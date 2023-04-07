class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp_sum = 0
        for i in range(0,len(nums)):
            nums[i] = nums[i] + temp_sum
            temp_sum = nums[i]
        print(nums)
        return nums
      
      
      
"""
Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

"""
