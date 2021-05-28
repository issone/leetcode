class Solution:
    def climbStairs(self, n: int) -> int:
        # 直接DP，新建一个字典或者数组来存储以前的变量，空间复杂度O(n)
        dp = {}
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = self.climbStairs(i - 1) + self.climbStairs(i - 2)
        return dp[n]

    def climbStairs2(self, n: int) -> int:
        # 还是DP，只不过是只存储前两个元素，减少了空间，空间复杂度O(1)

        if n == 1 or n == 2:
            return n
        first = 1
        second = 2
        for i in range(3, n + 1):
            first, second = second, first + second
        return second
