class Solution(object):
    def maxSubArray(self,nums):
        best_ending=res=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=nums[i]+best_ending
            best_ending=max(v1,v2)
            res=max(res,best_ending)
        return res

    def minSubArray(self,nums):
        best_ending=res=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=nums[i]+best_ending
            best_ending=min(v1,v2)
            res=min(res,best_ending)
        return res

    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v1=abs(self.maxSubArray(nums))
        v2=abs(self.minSubArray(nums))
        res=max(v1,v2)
        return res
