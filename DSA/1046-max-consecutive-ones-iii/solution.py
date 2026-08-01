class Solution(object):
    def longestOnes(self, nums, k):
        low=0
        n=len(nums)
        zero_count=ans=0
        for high in range(n):
            if nums[high]==0:
                zero_count+=1
            while zero_count>k:
                if nums[low]==0:
                    zero_count-=1
                low+=1
            length=high-low+1
            ans = max(ans, length)
        return ans