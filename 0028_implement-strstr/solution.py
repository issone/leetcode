class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_length, h_length = len(needle), len(haystack)
        if n_length > h_length:
            return - 1
        if n_length == 0:  # 空字符串返回0
            return 0
        ph = 0  # 指向haystack第一个元素位置
        while ph < h_length - n_length + 1:
            while ph < h_length - n_length + 1 and haystack[ph] != needle[0]:  # 移动ph指针，知道ph所指向的值与needle中的第一个值
                ph += 1
            pn = 0  # 指向needle子串第一个元素位置
            curr_length = 0
            while ph < h_length and pn < n_length and haystack[ph] == needle[pn]:
                ph += 1
                pn += 1
                curr_length += 1

            # 完全匹配，返回匹配子串的起始坐标
            if curr_length == n_length:
                return ph - curr_length

            #  不完全匹配，回溯， 使ph = ph-curr_length + 1 (因为之前已经从ph_curr_length，匹配过了，所以从下一个继续开始匹配) ,pn=0，curr_length=0
            ph = ph - curr_length + 1
        return -1
