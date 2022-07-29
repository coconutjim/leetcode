'''
83. Remove Duplicates from Sorted List
Easy

https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 
Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''
## --------------------------------------------------------------------------

'''
Solution

Using set to save unique values, and check next links

Time: O(n)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        s = set()
        s.add(curr.val)
        while curr.next:
            nxt = curr.next
            if nxt.val in s:
                curr.next = nxt.next
            else:
                s.add(nxt.val)
                curr = nxt
            s.add(curr.val)
        return head