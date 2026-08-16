class Solution:
    def subarraySum(self, nums, k):
        freq={}
        freq[0]=1
        s=c=0
        for i in range(len(nums)):
            s+=nums[i]
            ques=s-k
            c+=freq.get(ques,0)
            freq[s]=freq.get(s,0)+1
        return c