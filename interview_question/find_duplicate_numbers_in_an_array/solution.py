"""
题目1：在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
"""


def solution1(nums):
    """时间复杂度为O(n)，空间复杂度O(n)"""
    if nums is None or len(nums) <= 1:
        return -1
    d = set()
    for i in nums:
        if i in d:
            return i
        d.add(i)
    return -1


def solution2(nums):
    """长度为n,且数字的范围在0~n-1，如果没有重复值，则一个萝卜一个坑
    时间复杂度O(n),空间复杂度O(1)"""
    if nums is None or len(nums) <= 1:
        return -1
    i = 0
    while i < len(nums):
        if nums[i] == i:  # 索引和值相等，则这个位置有值（且是第一个值），继续往后看
            i += 1
        else:
            # 不等，则判断当前位置的值是否重复（正常情况，值(nums[i])应该与索引i相同，此时不同，则判断索引位置（此时的nums[i]）所对应的值与当前值（nums[i]）是否相同）
            if nums[nums[i]] == nums[i]:
                return nums[i]
            else:  # 如果不相等，则把当前值换到对应索引位置上（之前的位置上可能是一个其他值）
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return -1


"""
题目2：不修改数据找出重复的数字
在一个长度为n+1的数组里的所有数字都在1到n的范围内，所以数组中至少有一个数字是重复的
请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,5,4,3,2,6,7}，那么对应的输出是重复的数字2或者3。
你设计的解决方案必须不修改数组 nums 且只用常量级 O(1) 的额外空间。


"""


def solution3(nums):
    """
    如果用hash会很简单，空间复杂度为0(n）, 时间复杂度为O(n)，但是题目限制了空间复杂度为O(1)，所以不能考虑
    https://leetcode-cn.com/problems/find-the-duplicate-number/solution/er-fen-fa-si-lu-ji-dai-ma-python-by-liweiwei1419/

    因为有各种限制，才用二分这种耗时的做法

    二分法，时间复杂度O(nlogn)，空间复杂度O(1)

    把 1-n想象成n个抽屉，每个抽屉里装着对应值的数

    二分查找的思路是先猜一个数（有效范围 [left..right] 里位于中间的数 mid），然后统计原始数组中 小于等于 mid 的元素的个数 cnt：
    如果 cnt 严格大于 mid。根据抽屉原理，重复元素就在区间 [left..mid] 里；
    否则，重复元素就在区间 [mid + 1..right] 里。


    """
    left = 1  # 因为值是从1开始，所以没必要从0开始
    right = len(nums) - 1

    while left <= right:
        ctn = 0  # 放在这里是为了每次统计小于新mid的数字的数量
        mid = left + (right - left) // 2  # mid是值，不是索引
        for i in nums:
            if i <= mid:
                ctn += 1
        if ctn > mid:
            right = mid - 1
        else:
            left = mid + 1
    return left
