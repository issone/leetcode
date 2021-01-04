from typing import List

nums = [3, 4, 5, 1, 2]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]

        left = 0
        right = length - 1
        if nums[right] > nums[0]:  # 最右边比最左边大，说明整个有序，直接返回第一个
            return nums[0]

        # 因为旋转后，两段都各自有序，所以旋转点的左边第一个值，比旋转点右边的任意值都大
        # 旋转点的特点：
        # 旋转点左侧所有元素 > 数组第一个元素
        # 旋转点右侧所有元素 < 数组第一个元素
        # 所以，如果中间元素 > 数组第一个元素，说明旋转点在中间位置mid的右方，即 当nums[mid]>num[0]有，left=mid+1
        # 如果中间元素 < 数组第一个元素，说明旋转点在中间位置mid或其左方，即 当nums[mid]<>num[0]有，right=mid-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:  # 中值比最左大，说明是有序，旋转点在右方
                left = mid + 1
            else:  # 中值比最左小，说明是倒序，旋转点在mid或其右方， right 更新时会被设为 mid 而不是 mid-1，因为 mid 无法被排除
                right = mid
