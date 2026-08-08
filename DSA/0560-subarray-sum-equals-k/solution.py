class Solution:
    def subarraySum(self, nums, k):
        freq = {0: 1}
        count = 0
        sumi = 0
        for i in range(len(nums)):
            sumi += nums[i]
            ques = sumi - k
            count += freq.get(ques, 0)
            freq[sumi] = freq.get(sumi, 0) + 1
        return count