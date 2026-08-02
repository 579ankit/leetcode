class Solution:
    def subarraySum(self, nums, k):
        d = {}
        d[0] = 1
        s = 0
        count = 0
        for num in nums:
            s += num
            ques = s - k
            if ques in d:
                count += d[ques]
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        return count