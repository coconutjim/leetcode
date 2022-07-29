'''
1287. Element Appearing More Than 25% In Sorted Array
Easy

https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:
Input: arr = [1,1]
Output: 1

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
'''
## --------------------------------------------------------------------------

'''
Solution

Using counter

Time: O(n)
'''
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = Counter()
        for n in arr:
            counter[n] += 1
        L = len(arr)
        for k, v in counter.items():
            if v > 0.25 * L:
                return k