from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """

        顺序扫描数组，判断目标值与当前元素的差值，在 map 中是否存在。
        如果存在，直接返回 2 个数字的下标。
        如果不存在，就把这个数字存入 map 中作为key，下标作为value
        进入下一次循环等待扫到“另一半”数字的时候，再取出来返回结果。
        :param nums:
        :param target:
        :return:
        """
        dit = {}
        for index, num in enumerate(nums):
            if num not in dit:
                dit[target - num] = index
            else:
                return [dit[num], index]

