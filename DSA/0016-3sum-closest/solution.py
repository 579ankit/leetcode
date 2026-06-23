class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        max_diff=float('inf')
        res_sum=0
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                total = nums[i]+nums[left]+nums[right]
                diff=abs(total-target)
                if diff<max_diff:
                    max_diff=diff
                    res_sum=total
                if total==target:
                    return res_sum
                elif total>target:
                    right-=1
                else:
                    left+=1
        return res_sum
    
