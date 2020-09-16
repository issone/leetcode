class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right, ans = -1, 0  # right为右指针，-1代表还没移动过
        sets = set()  # 记录出现过的每个字符
        n = len(s)
        for i in range(n):  # 遍历每个元素，判断以当前元素作为起始位置时的子串情况
            if i != 0:  # i是左指针，左指针每移动一次，移除最左边的一个字符,判断剩余子串中的情况
                sets.remove(s[i - 1])

            while right + 1 < n and s[right + 1] not in sets:  # 没有重复值时, 移动右指针
                right += 1
                sets.add(s[right])
            # 遇到重复的
            ans = max(ans, right - i + 1)  # i到right之间是一个无重复的子串
        return ans


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 保存最大长度
        max_l = 0
        # 该字段维护每个字符最新出现的下标
        # 例如 a b c (a) 第二个a是最新出现的，下标为3
        c_dict = {}
        # k表示当前不重复子串的起始位置
        k = -1

        for i, c in enumerate(s): # 从头遍历字符串

            if c in c_dict and c_dict[c] > k:
                # 如果c出现重复，即c在c_dict
                # 同时如果"c上次出现时的下标大于当前子串的起始位置"
                # 更新起始位置
                k = c_dict[c]

            else:
                # 否则
                # i - k 即为不重复子串的长度，于之前的最大长度做对比，谁大选谁
                max_l = max(max_l, i - k)
            # 更新字符最新出现的下标
            c_dict[c] = i

        return max_l
