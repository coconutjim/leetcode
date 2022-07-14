'''
1. Two Sum
Easy

https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
'''
## --------------------------------------------------------------------------

'''
Solution

In sorted array, we can find result by O(n):
2 pointers from left and right, if sum is less than target, we move the left one, otherwise the right one.

Time: O(n*log n) because of sorting
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
		# We have to sort indicies to
        ind = sorted(range(len(nums)), key=lambda k: nums[k])
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i != j:
            a = nums[i]
            b = nums[j]
            if a + b == target:
                return [ind[i], ind[j]]
            if a + b > target:
                j -= 1
            else:
                i += 1
        return []