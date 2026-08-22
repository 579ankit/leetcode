class Solution(object):
    def fun(self,s,i,n):
        if i>=n-1:
            return True
        if s[i]!=s[n-1]:
            return False
        return self.fun(s,i+1,n-1)

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        normalized=''
        for ch in s:
            if ch.isalnum():
                normalized+=ch.lower()
        return self.fun(normalized,0,len(normalized))
