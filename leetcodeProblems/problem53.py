# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         max_sum = -1000000
#         temp=0
#         if(len(nums)==1):
#             return nums[0]
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 temp = 0
#                 for k in range(i,j+1):
#                     temp+=nums[k]
#                 if(max_sum < temp):
#                     max_sum = temp
#                     # print(temp)
#         return max_sum 

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """      
        max_subarray = nums[0]
        sum = 0
        for i in range(len(nums)):
            if(sum < 0):
                sum = 0
            sum += nums[i]
            max_subarray = max(max_subarray, sum)
        return max_subarray