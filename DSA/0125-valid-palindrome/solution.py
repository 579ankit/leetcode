class Solution(object):
    def checkPallindrome(self,s,low,high):
        if low >= high:
            return True
        if s[low] != s[high]:
            return False
        return self.checkPallindrome(s,low+1,high-1)

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low=0
        normalized = ""
        for ch in s:
            if ch.isalnum():
                normalized += ch.lower()
        high=len(normalized)-1
        return self.checkPallindrome(normalized,low,high)