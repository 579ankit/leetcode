class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        last_index = {}
        max_len = 0

        for right, ch in enumerate(s):
            # if char already in window, move left pointer
            if ch in last_index and last_index[ch] >= left:
                left = last_index[ch] + 1

            last_index[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len
