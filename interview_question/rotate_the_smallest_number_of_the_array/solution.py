from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        length = len(numbers)
        left = 0
        right = length - 1

        while left < right:
            mid = (right - left) // 2 + left

            if numbers[mid] < numbers[right]:  # 说明最小值在[left, mid]
                left = mid + 1
            elif numbers[mid] > numbers[right]:  # 说明最小值在[mid+1,right]
                right = mid
            else:  # numbers[mid] = numbers[right] 应继续往左找，可能有更小的值
                right -= 1
        return numbers[left]
