class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return True
        low=0
        high=num
        while low<=high:
            guess=(low+high)//2
            square=guess*guess

            if num==square:
                return True
            elif num>square:
                low=guess+1
            else:
                high=guess-1
        return False