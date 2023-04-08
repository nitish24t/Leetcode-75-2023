class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub_index = 0
        if s == "":
            return True
        for i,elem in enumerate(t):
            if sub_index >= len(s):
                break
            if elem == s[sub_index]:
                sub_index += 1
        
        if sub_index == len(s):
            return True
        else:
            return False
          
          
"""
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
""" 
