class Solution(object):
    def fun(self, curr, open_count, close_count, n, res):
        if open_count == n and close_count == n:
            res.append(curr)
            return
        if open_count < n:
            self.fun(curr + "(", open_count + 1, close_count, n, res)
        if close_count < open_count:
            self.fun(curr + ")", open_count, close_count + 1, n, res)

    def generateParenthesis(self, n):
        res = []
        self.fun("", 0, 0, n, res)
        return res