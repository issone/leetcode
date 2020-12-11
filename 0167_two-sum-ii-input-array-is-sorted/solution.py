from typing import List


class Solution:
    """
    二分查找
    时间复杂度：O(nlogn)，其中 n是数组的长度。需要遍历数组一次确定第一个数，时间复杂度是 O(n)，寻找第二个数使用二分查找，时间复杂度是 O(logn)，因此总时间复杂度是 O(nlogn)。
    空间复杂度：O(1)
    在数组中找到两个数，使得它们的和等于目标值，可以首先固定第一个数，然后寻找第二个数，第二个数等于目标值减去第一个数的差。
    利用数组的有序性质，可以通过二分查找的方法寻找第二个数。
    为了避免重复寻找，在寻找第二个数时，只在第一个数的右侧寻找。
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            low, high = i + 1, n - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] > target - numbers[i]:
                    high = mid - 1
                else:
                    low = mid + 1

        return [-1, -1]

