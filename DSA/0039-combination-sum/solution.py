class Solution(object):
    def fun(self, candidates, idx, target, curr_sum, res, diary):

        if idx == len(candidates):
            if curr_sum == target:
                res.append(diary[:])
            return

        # NOT TAKE
        self.fun(candidates, idx + 1, target, curr_sum, res, diary)

        # TAKE
        if candidates[idx] + curr_sum <= target:
            diary.append(candidates[idx])
            curr_sum += candidates[idx]

            self.fun(candidates, idx, target, curr_sum, res, diary)

            diary.pop()
            curr_sum -= candidates[idx]

    def combinationSum(self, candidates, target):
        curr_sum = 0
        idx = 0
        res = []
        diary = []

        self.fun(candidates, idx, target, curr_sum, res, diary)

        return res