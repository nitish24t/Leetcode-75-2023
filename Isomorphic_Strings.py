class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for x,y in zip(s,t):
            if s.index(x) != t.index(y):
                return False
        return True
      

"""
Description : Two strings s and t are isomorphic if the characters in s can be replaced to get t.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""
