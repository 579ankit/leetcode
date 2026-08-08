class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq={0:1}
        count=0
        sumi=0
        for i in range(len(nums)):
            sumi+=nums[i]
            ques=sumi%k
            if ques<0:
                ques+=k
            count+=freq.get(ques,0)
            freq[ques]=freq.get(ques,0)+1
        return count