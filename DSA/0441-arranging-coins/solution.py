class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=0
        high=n
        while low<=high:
            guess=(low+high)//2
            coins = guess*(guess+1)//2
            if coins==n:
                return guess
            elif coins>n:
                high=guess-1
            else:
                low=guess+1
        return high