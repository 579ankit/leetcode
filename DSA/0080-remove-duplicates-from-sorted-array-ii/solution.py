class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)==2:
            return len(nums)
        off,cm=2,2
        while cm<len(nums):
            if nums[cm]==nums[off-2]:
                cm+=1
            else:
                nums[off]=nums[cm]
                off+=1
                cm+=1
        return off
