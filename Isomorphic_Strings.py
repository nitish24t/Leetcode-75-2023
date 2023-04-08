class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        mem_s = {}
        mem_t = {}
        for i in range(0,n):
            if s[i] not in mem_s:
                mem_s[s[i]] = [i]
            else:
                mem_s[s[i]].append(i)

            if t[i] not in mem_t:
                mem_t[t[i]] = [i]
            else:
                mem_t[t[i]].append(i)
            # print("elems : {0}:{1}, \t count: {2},{3}".format(s[i], t[i], mem_s[s[i]], mem_t[t[i]]))
            if mem_s[s[i]] != mem_t[t[i]]:
                return False
        # print(mem_s)
        # print(mem_t)
        if len(mem_s) != len(mem_t):
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
