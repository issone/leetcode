from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:  # 找到target后，继续往左找（确定开始位置）
                right = mid
            else:
                right = mid - 1
        # 退出循环时，
        if nums[left] != target:  # 没有找到target，直接返回
            return [-1, -1]
        l2 = left  # 如果找到了target,此时target是开始位置，从开始位置往后找
        r2 = len(nums) - 1
        while l2 <= r2:
            m2 = (r2 - l2) // 2 + l2
            if nums[m2] == target:
                l2 = m2 + 1
            elif nums[m2] > target:
                r2 = m2 - 1
        # 终止时， 最后一个target是在l2的前面
        return [left, l2 - 1]
