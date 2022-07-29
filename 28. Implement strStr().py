'''
28. Implement strStr()
Easy

https://leetcode.com/problems/implement-strstr/

Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
 

Constraints:
1 <= haystack.length, needle.length <= 10^4
haystack and needle consist of only lowercase English characters.
'''
## --------------------------------------------------------------------------

'''
Solution

Iterative substring approach

Time: O(n * m)
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        if length == 0:
            return 0
        for i in range(0, len(haystack) - length + 1):
            if haystack[i : i + length] == needle:
                return i
        return -1