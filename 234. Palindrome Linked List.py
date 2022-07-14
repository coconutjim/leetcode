'''
234. Palindrome Linked List
Easy

https://leetcode.com/problems/palindrome-linked-list/

Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
'''

'''
Solution

We take 2 pointers, first is 2x faster than second, and traverse the list
The second pointer reverses elements
When the first reaches the end, the second reverses half of a list
Then we just need to compare two halfs (middle odd element must be ommited)

Time: O(n)
Space: O(1)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
	# If 1 element, return True
        if not head.next:
            return True
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
 
        if fast:
            slow = slow.next
            
        while slow:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
        return True
