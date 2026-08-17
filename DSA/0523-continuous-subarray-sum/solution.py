class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        freq={0:-1}
        prefix_sum=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            ques=prefix_sum%k
            if ques in freq:
                if i-freq[ques]>=2:
                    return True
            else:
                freq[ques]=i
        return False