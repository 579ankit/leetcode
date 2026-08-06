class Solution(object):
    def fun(self, a, n, idx, diary, res, curr_sum, target):
        if idx == n:
            if curr_sum == target:
                res.append(diary[:])
            return
        # Not take
        self.fun(a, n, idx + 1, diary, res, curr_sum, target)
        # Take
        if curr_sum + a[idx] <= target:
            diary.append(a[idx])
            curr_sum+=a[idx]
            self.fun(a, n, idx, diary, res, curr_sum, target)
            diary.pop()
            curr_sum-=a[idx]

    def combinationSum(self, candidates, target):
        n=len(candidates)
        res,diary=[],[]
        idx=0
        curr_sum=0
        self.fun(candidates, n, idx, diary, res, curr_sum, target)
        return res