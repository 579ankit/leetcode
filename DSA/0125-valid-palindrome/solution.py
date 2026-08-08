class Solution(object):
    def fun(self,s,n,low,high):
        if low>=high:
            return True
        if s[low]!=s[high]:
            return False
        return self.fun(s,n,low+1,high-1)


    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        normalized=""
        for ch in s:
            if ch.isalnum():
                normalized += ch.lower()
        n=len(normalized)
        return self.fun(normalized,n,0,n-1)