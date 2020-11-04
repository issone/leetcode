class Solution:
    def pivotIndex(self, nums) -> int:
        """
        当存在中心索引时,
        假设mid_val为中心索引的值, left_sum为左侧数组元素和， right_sum为右侧数组元素和， count为数组中所有元素和，
        一定有以下条件成立
        1. left_sum + right_sum + mid_val = count
        2. left_sum = right_sum
        即 2*left_num = count - mid_val

        :param nums:
        :return:
        """
        count = sum(nums)
        left_sum = 0
        for index, val in enumerate(nums):
            if 2 * left_sum == count - val:
                return index
            left_sum += val
        return -1
