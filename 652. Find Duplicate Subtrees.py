'''
652. Find Duplicate Subtrees
Medium

https://leetcode.com/problems/find-duplicate-subtrees/

Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.
 

Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:
Input: root = [2,1,1]
Output: [[1]]

Example 3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 

Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
'''
## --------------------------------------------------------------------------

'''
Solution

Preorder traversal (recursive) and add path to string.
Save paths in dict (Counter)
Add only when counter == 2 to get any of the duplicates

Time: O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node, paths, res):
        if node is None:
            return '#'
        path = ''
        path += '{} {} {}'.format(str(node.val),
                            self.inorder(node.left, paths, res), 
                            self.inorder(node.right, paths, res))
        paths[path] += 1
        if paths[path] == 2:
            res.append(node)
        return path
    
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        paths = Counter()
        res = []
        self.inorder(root, paths, res)
        return res