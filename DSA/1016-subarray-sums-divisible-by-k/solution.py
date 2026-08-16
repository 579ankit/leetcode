class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq={0:1}
        s=c=0
        for i in range(len(nums)):
            s+=nums[i]
            ques=s%k
            if ques<0:
                ques+=k
            c+=freq.get(ques,0)
            freq[ques]=freq.get(ques,0)+1
        return c