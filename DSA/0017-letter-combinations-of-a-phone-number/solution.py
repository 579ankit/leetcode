class Solution(object):
    def fun(self,s,n,diary,res,idx):
        if idx==n:
            res.append(''.join(diary))
            return
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        choice=phone[s[idx]]
        for i in range(len(choice)):
            diary.append(choice[i])
            self.fun(s,n,diary,res,idx+1)
            diary.pop()
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        res,diary=[],[]
        self.fun(digits,len(digits),diary,res,0)
        return res