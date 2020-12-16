from typing import List


class Solution:
    """
    前缀和 + 二分查找
    时间复杂度：O(nlogn)，其中 n 是数组的长度。需要遍历每个下标作为子数组的开始下标，遍历的时间复杂度是 O(n)，
             对于每个开始下标，需要通过二分查找得到长度最小的子数组，二分查找得时间复杂度是 O(logn)，因此总时间复杂度是O(nlogn)。
    空间复杂度：O(n)，其中 n 是数组的长度。额外创建数组sums 存储前缀和。

    """

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        ans = n + 1
        sums = [0]  # 用于存储数组 nums 的前缀和，其中sums[i] 表示从 nums[0] 到 nums[i−1] 的元素和。 这道题保证了数组中每个元素都为正，所以前缀和一定是递增的

        for i in range(n):
            sums.append(sums[-1] + nums[i])

        for i in range(1, n + 1):
            target = s + sums[i - 1]
            # 通过二分查找得到大于或等于i 的最小下标 bound，使得sums[bound]−sums[i−1]≥s，并更新子数组的最小长度（此时子数组的长度是 bound−(i−1)）。
            bound = self.bisect_left(sums, 0, len(sums) - 1, target)
            if bound != len(sums):
                ans = min(ans, bound - (i - 1))

        return 0 if ans == n + 1 else ans

    def bisect_left(self, nums: list, left: int, right: int, target: int):
        """通过二分查找得到nums中大于或等于 target 的最小下标"""

        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
