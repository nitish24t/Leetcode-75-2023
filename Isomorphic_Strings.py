class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mem_s = []
        mem_t = []
        for elem in s:
            mem_s.append(s.index(elem))
        for elem in t:
            mem_t.append(t.index(elem))
        print(mem_s)
        print(mem_t)
        if mem_s == mem_t:
            return True
        return False
      

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
