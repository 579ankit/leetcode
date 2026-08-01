class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False

        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        if n==1:
            return True 
        return False