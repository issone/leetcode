class Solution:
    def numWays(self, n: int) -> int:
        """时间复杂度和空间复杂度都是O(n)"""
        dp = [1, 1]
        for i in range(2, n + 1):
            dp.append((dp[i - 1] + dp[i - 2]) % 1000000007)
        return dp[n]
