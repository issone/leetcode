from typing import List


class Solution:
    """
    不需要额外空间的方法，就往位运算上想
    异或：相同为0，不同为1. 异或同一个数两次，原数不变。
    """
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a = a ^ num
        return a