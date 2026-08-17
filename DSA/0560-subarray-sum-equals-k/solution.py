class Solution:
    def subarraySum(self, nums, k):
        freq={0:1}
        prefix_sum=count=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            ques=prefix_sum-k
            count+=freq.get(ques,0)
            freq[prefix_sum]=freq.get(prefix_sum,0)+1
        return count