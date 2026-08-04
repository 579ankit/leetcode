class Solution(object):
    def reverse(self,nums,low,high):
        while low<high:
            nums[low],nums[high]=nums[high],nums[low]
            low+=1
            high-=1
        return nums
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
        return nums