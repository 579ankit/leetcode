class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d={}
        s=res=0
        d[0]=1
        for num in nums:
            s+=num
            ques=s%k
            if ques<0:
                ques+=k
            res+=d.get(ques,0)
            d[ques]=d.get(ques,0)+1
        return res