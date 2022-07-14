'''
53. Maximum Subarray
Medium

https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:

1 <= nums.length <= 10^5
-104 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
## --------------------------------------------------------------------------

'''
Solution

Dynamic programming: iteratively save max sum for any element

Time: O(n)
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = []
        sums.append(nums[0])
        res = sums[0]
        for i in range(1, len(nums)):
            sums.append(max(sums[i - 1] + nums[i], nums[i]))
            if sums[i] > res:
                res = sums[i]
        return res