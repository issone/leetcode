from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dit = {}
        for index, num in enumerate(nums):
            if num not in dit:
                dit[target - num] = index
            else:
                return [dit[num], index]

