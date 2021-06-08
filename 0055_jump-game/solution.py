from typing import List


class Solution:
    """
    从后往前推
    记录一个的坐标代表当前可达的最后节点，这个坐标初始等于nums.length-1，
    然后我们每判断完是否可达，都向前移动这个坐标，直到遍历结束。
    如果这个坐标等于0，那么认为可达，否则不可达。
    """

    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        i = last_position = len(nums) - 1

        while i >= 0:
            # nums[i] 可走的最大步数，i是当前位置
            if nums[i] + i >= last_position:  # 能到达最后的节点
                i -= 1
            else:
                break
        if i != 0:
            return False
        return True
