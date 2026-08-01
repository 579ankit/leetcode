class Solution(object):
    def recursion(self,num):
        s=0
        while num>0:
            d=num%10
            s=s+d
            num//=10
        return s

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            num = self.recursion(num)
        return num
