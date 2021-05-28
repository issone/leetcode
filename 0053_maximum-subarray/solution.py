from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        max_num = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])  # 留大的，dp[i-1] + nums[i]如果小于nums[i]，说明nums[i]为负数
            max_num = max(max_num, dp[i])

        return max_num

    def maxSubArray2(self, nums: List[int]) -> int:
        # 上面的方法存在优化空间， 观察上面可以发现，dp[i]的结果只和上次的结果有关，
        n = len(nums)
        max_num = pre = nums[0]
        for i in range(1, n):
            pre = max(pre + nums[i], nums[i])  # 留大的，dp[i-1] + nums[i]如果小于nums[i]，说明nums[i]为负数
            max_num = max(max_num, pre)

        return max_num
