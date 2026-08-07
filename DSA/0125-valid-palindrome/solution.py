class Solution(object):
    def checkPalindrome(self, s, low, high):
        if low >= high:
            return True
        if not s[low].isalnum():
            return self.checkPalindrome(s, low + 1, high)
        if not s[high].isalnum():
            return self.checkPalindrome(s, low, high - 1)
        if s[low].lower() != s[high].lower():
            return False
        return self.checkPalindrome(s, low + 1, high - 1)

    def isPalindrome(self, s):
        return self.checkPalindrome(s, 0, len(s) - 1)