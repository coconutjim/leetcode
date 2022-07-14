'''
1299. Replace Elements with Greatest Element on Right Side
Easy

https://leetcode.com/problems/palindrome-linked-list/
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
After doing so, return the array.
 

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:
Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
'''
## --------------------------------------------------------------------------

'''
Solution

First, we traverse from the right and save maximums with their positions into a stack
Then we use stack to inflate new array

Time: O(n)
'''

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        if l == 1:
            return [-1]
        max_vals = []
        max_val = arr[l - 1]
        max_vals.append((max_val, l - 1))
        for i in range(l - 1, -1, -1):
            if arr[i] > max_val:
                max_vals.append((arr[i], i))
                max_val = arr[i]
        res = []
        step = 0
        while(max_vals):
            max_val = max_vals.pop()
            val = max_val[0]
            index = max_val[1]
            for i in range(index - step):
                res.append(val)
            step = index
        res.append(-1)
        return res