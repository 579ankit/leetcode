class Solution(object):
    def fun(self,nums,res,diary,idx,n):
        if idx==n:
            res.append(diary[:])
            return
        for i in range(n):
            if nums[i] in diary:
                continue
            diary.append(nums[i])
            self.fun(nums,res,diary,idx+1,n)
            diary.pop()
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res,diary=[],[]
        n=len(nums)
        idx=0
        self.fun(nums,res,diary,idx,n)
        return res
        