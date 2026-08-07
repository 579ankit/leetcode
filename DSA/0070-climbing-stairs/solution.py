class Solution(object):
    def climbStairs(self, n,memo={}):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        prev0=1
        prev1=2
        for i in range(3,n+1):
            temp=prev0+prev1
            prev0=prev1
            prev1=temp
        return prev1