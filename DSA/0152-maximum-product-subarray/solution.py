class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_ending=max_ending=ans=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=min_ending*nums[i]
            v3=max_ending*nums[i]
            best_ending=max(v1,max(v2,v3))
            ans=max(ans,best_ending)
            min_ending=min(v1,min(v2,v3))
            max_ending=max(v1,max(v2,v3))
        return ans