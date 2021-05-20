class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        答题思路：从后往前寻找第一个升序对(i,j)即nums[i]<nums[j] 再从后往前找第一个大于nums[i]的数即为大数，交换着两个元素即将大数换到前面，然后将大数后面的部分倒序
        """
        n = len(nums)
        if n < 2:
            return nums
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:  # 从后往前找第一个相邻升序元素对
            i -= 1
        if i == 0:  # 此数为最大数，则需要倒排
            nums.reverse()
        else:
            j = n - 1   # 此时的num[i] > num[i-1], 且i是拐点， [i,n) 为降序
            while j >= i and nums[j] <= nums[i - 1]:    # 从后往前找，找到第一个大于num[i-1]的值并进行交换 （这样找的值交换后，增幅最小）
                j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]

            # 逆序
            for k in range((n - i) // 2):
                nums[i + k], nums[n - 1 - k] = nums[n - 1 - k], nums[i + k]



