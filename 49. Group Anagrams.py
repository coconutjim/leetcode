'''
49. Group Anagrams
Medium

https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
## --------------------------------------------------------------------------

'''
Solution

Sort all of groups and save to a dict with lists (with key = sorted group)

Time: O(n)
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total = defaultdict(list)
        for s in strs:
            srt = ''.join(sorted(s))
            total[srt].append(s)
        return [v for v in total.values()]