'''
541. Reverse String II
Easy

https://leetcode.com/problems/reverse-string-ii/

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"

Constraints:

1 <= s.length <= 10^4
s consists of only lowercase English letters.
1 <= k <= 10^4
'''
## --------------------------------------------------------------------------

'''
Solution

Traverse the string with step k, copy chars in original or reverse order alternatively

Time: O(n)
'''

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = len(s)
        res = ''
        left = 0
        flg = True
        while (left < l):
            right = min(left + k - 1, l - 1)
            if flg:
                res += ''.join([s[j] for j in range(right, left - 1, -1)])
            else:
                res += s[left: right + 1]
            flg = not flg
            left += k
        return res
