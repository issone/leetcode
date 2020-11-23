from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """纵向扫描
            停止扫描的情况：
            1.最长公共前缀的最大长度<= 数组中最短字符串长度
            2.按列比较，值不相等，则停止

        """
        if not strs:
            return ""
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            for j in range(1, count):
                if len(strs[j]) == i or c != strs[j][i]:
                    return strs[0][:i]
        return strs[0]
