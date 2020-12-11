from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """因为题目给定的条件是，nums的长度为偶数，要是min(ai,bi)总和最大，即要求
        每个划分之后的数组中的最小值和为最大，那么也就是说我们要让每个划分之后的数组
        的最小值尽量最大化，通俗点说，就是要让最大的和倒数第二大的在一个小数组里面，
        这样就可以发挥出倒数第二大的优势，所以先进行排序，然后取奇数和即可
        """
        nums.sort()
        res = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                res += nums[i]
        return res
