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
            low, high = i + 1, n - 1    # low 开始的时候为i+1是为了，保证数组长度为偶数时，mid得到的是后面那个元素，避免mid和i重复
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]  # 因为返回的下表不是从0开始，所以在原基础上+1
                elif numbers[mid] > target - numbers[i]:
                    high = mid - 1
                else:
                    low = mid + 1

        return [-1, -1]


class Solution2:
    """
     哈希表
    首先设置字典dict={},然后通过enumerate函数对numbers迭代，index代表索引，num代表索引对应的值。
    先看最后面，[target-num]作为dict的键，index作为值。
    这样if判断只需要判断num是否在dict中，如果在的话，通过dict[num]找到之前的num对应的index，那么就可以返回[dict[num]+1,index+1],
    不在的话就更新字典，target-num代表着下一个需要的数字，而迭代的num就是下一个数字，以此来判断。
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = dict()
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if tmp in dic:
                return [dic[tmp] + 1, i + 1]
            dic[numbers[i]] = i
        return [-1, -1]
