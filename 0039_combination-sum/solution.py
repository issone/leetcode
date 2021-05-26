from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        end = len(candidates)

        def dfs(start, path, target):
            if target < 0:  # 不符合条件的剪枝
                return
            if target == 0:  # 将符合条件的保存
                res.append(path)
                return
            for i in range(start, end):
                cur = candidates[i]
                dfs(i, path + [cur], target - cur)

        dfs(0, [], target)
        return res

