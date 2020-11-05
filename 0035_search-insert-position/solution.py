from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size == 0:
            return 0

        # 特判
        if nums[-1] < target:
            return size

        left = 0
        right = size - 1

        while left < right:
            # left + right 在 Python 中如果发生整型溢出，Python 会自动转成长整形
            mid = (left + right) // 2
            # 严格小于 target 的元素一定不是解
            if nums[mid] < target:
                # 下一轮搜索区间是 [mid + 1, right]
                left = mid + 1
            else:
                # 下一轮搜索区间是 [left, mid]
                right = mid
        return left     # 终止条件 left=right
