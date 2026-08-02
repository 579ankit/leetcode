class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zero,one=0,0
        d={}
        res=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else:
                one+=1
            diff=zero-one
            if diff==0:
                res=max(res,i+1)
            elif diff in d:
                res=max(res,i-d[diff])
            else:
                d[diff]=i
        return res