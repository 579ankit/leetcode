class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        for i in nums:
            if i!=val:
                nums[c]=i
                c+=1
        return c

