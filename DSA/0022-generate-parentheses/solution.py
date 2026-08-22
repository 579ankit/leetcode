class Solution(object):
    def fun(self,n,curr,open_count,close_count,res):
        if open_count==n and close_count==n:
            res.append(curr)
            return
        if open_count<n:
            self.fun(n,curr+'(',open_count+1,close_count,res)
        if close_count<open_count:
            self.fun(n,curr+')',open_count,close_count+1,res)
        return

    def generateParenthesis(self, n):
        res=[]
        self.fun(n,'',0,0,res)
        return res