class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low = 0
        high = k - 1
        s = 0
        res = 0
        freq = {}

        for i in range(low, high + 1):
            s += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        while high < len(nums):
            if len(freq) == k:
                res = max(res, s)
            # Remove left element
            x = nums[low]
            freq[x] -= 1

            if freq[x] == 0:
                del freq[x]
            low += 1
            high += 1
            if high == len(nums):
                break
            s -= x
            x = nums[high]
            freq[x] = freq.get(x, 0) + 1
            s += x
        return res