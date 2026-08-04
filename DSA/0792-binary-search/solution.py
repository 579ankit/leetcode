class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low,high=0,len(nums)-1
        while low<=high:
            guess=(low+high)//2
            if nums[guess]==target:
                return guess
            elif nums[guess]>target:
                high=guess-1
            else:
                low=guess+1
        return -1