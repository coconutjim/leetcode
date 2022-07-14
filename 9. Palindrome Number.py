'''
9. Palindrome Number
Easy

https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
 

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-2^31 <= x <= 2^31 - 1
 

Follow up: Could you solve it without converting the integer to a string?
'''
## --------------------------------------------------------------------------

'''
Solution

Negative number is always not a palindrome.
For others, we create an array with digits by dividing and saving mods.
Then use 2 pointers from left and right to compare.

Time: O(n)
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digits = []
        while x > 9:
            digits.append(x % 10)
            x = x // 10
        digits.append(x)
        i = 0
        j = len(digits) - 1
        while i < j:
            if digits[i] != digits[j]:
                return False
            i += 1
            j -= 1
        return True