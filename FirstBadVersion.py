# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            mid_check = isBadVersion(mid)
            print("Left:{0}\tRight:{1}\tmid:{2}\tmid_check:{3}".format(left,right,mid,mid_check))
            if mid_check:
                right = mid
            else:
                left = mid + 1
        return left
      
      
"""
Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.


Example 2:

Input: n = 1, bad = 1
Output: 1
"""
