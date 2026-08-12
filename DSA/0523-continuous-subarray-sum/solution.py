class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        freq = {0: -1}
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            rem = prefix_sum % k
            if rem in freq:
                if i - freq[rem] > 1:
                    return True
            else:
                freq[rem] = i
        return False
