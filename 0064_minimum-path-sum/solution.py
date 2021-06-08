from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        if not n:
            return 0
        # 状态定义：dp[i] 表示从 (0, 0) 到达第 i - 1 行的最短路径值
        dp = [0] * n
        # 状态初始化
        dp[0] = grid[0][0]
        # 状态转移
        for i in range(m):
            for j in range(n):
                if i == 0 and j != 0:  # 顶部横着计算， 前一列的值 + 当前位置的值
                    dp[j] = dp[j - 1] + grid[i][j]
                elif i != 0 and j == 0:  # 左侧竖着计算， dp[j]是上一行的值 + 当前位置的值
                    dp[j] = dp[j] + grid[i][j]
                elif i != 0 and j != 0:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]
