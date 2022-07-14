'''
540. Single Element in a Sorted Array
Medium

https://leetcode.com/problems/palindrome-linked-list/

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

 

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
'''
## --------------------------------------------------------------------------

'''
Solution

The idea is that before single element arr[n] = arr[n+1] where n is even, and after arr[n] = arr[n+1] where n is odd
So we can user binary search

Time: O(log n)
Space: O(1)
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while (i < j):
            k = (i + j) // 2
            if k % 2 == 1:
                k -= 1
            if nums[k] == nums[k + 1]:
                i = k + 2
            else:
                j = k - 1
        return nums[i]