class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        i,j=0,n-1
        a=[0]*n
        k=n-1
        while i<=j:
            isq=nums[i]*nums[i]
            jsq=nums[j]*nums[j]
            if isq>jsq:
                a[k]=isq
                i+=1
            else:
                a[k]=jsq
                j-=1
            k-=1
        return a
