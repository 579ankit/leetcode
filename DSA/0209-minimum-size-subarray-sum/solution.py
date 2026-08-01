class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        low=0
        n=len(nums)
        s=0
        res=float('inf')
        for high in range(n):
            s=s+nums[high]
            while s>=target:
                length=high-low+1
                res=min(res,length)
                s=s-nums[low]
                low+=1
        if res==float('inf'):
            return 0
        else:
            return res