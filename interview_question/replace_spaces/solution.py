class Solution(object):
    def replaceSpace(self, s):
        """
        时间复杂度和空间复杂度都是O(n)
        """
        list_s = list(s)

        # 记录原本字符串的长度
        original_end = len(s)

        # 将空格改成%20 使得字符串总长增长 2n，n为原本空格数量。
        # 所以记录空格数量就可以得到目标字符串的长度
        n_space = 0
        for ss in s:
            if ss == ' ':
                n_space += 1

        list_s += ['0'] * 2 * n_space

        # 设置左右指针位置
        left, right = original_end - 1, len(list_s) - 1

        # 循环直至左指针越界
        while left >= 0:
            if list_s[left] == ' ':
                list_s[right] = '0'
                list_s[right - 1] = '2'
                list_s[right - 2] = '%'
                right -= 3
            else:
                list_s[right] = list_s[left]
                right -= 1

            left -= 1

        # 将list变回str，输出
        s = ''.join(list_s)
        return s
