from typing import List


class Solution:
    """
    双指针
    时间复杂度：O(n)，假设数组总共有 n 个元素，slow 和 fast至少遍历 2n 步
    空间复杂度：O(1)
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow


class Solution2:
    """
    双指针 —— 当要删除的元素很少时
    当我们遇到 nums[i] = val 时，我们可以将当前元素与最后一个元素进行交换，并释放最后一个元素。这实际上使数组的大小减少了 1。
    请注意，被交换的最后一个元素可能是想要移除的值。但是不要担心，在下一次迭代中，我们仍然会检查这个元素。

    时间复杂度：O(n)，i 和 n 最多遍历 n 步。在这个方法中，赋值操作的次数等于要删除的元素的数量。因此，如果要移除的元素很少，效率会更高
    空间复杂度：O(1)
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n
