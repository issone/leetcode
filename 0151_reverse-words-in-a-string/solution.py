class Solution:
    def reverseWords(self, s: str) -> str:
        l = self.trim_spaces(s)

        # 翻转字符串
        self.reverse(l, 0, len(l) - 1)

        # 翻转每个单词
        self.reverse_each_word(l)

        return ''.join(l)

    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1
        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1

        output = []
        # 将字符串间多余的空白字符去除
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':  # 最后一个元素不是空字符串时，才能继续填入空字符串
                output.append(s[left])
        return output

    def reverse(self, l: list, left: int, right: int) -> None:
        """翻转完成后单词是反的"""
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: list) -> None:
        """翻转单词"""
        n = len(l)
        start = end = 0

        while start < n:
            # 循环至单词的末尾
            while end < n and l[end] != ' ':
                end += 1
            # 翻转单词
            self.reverse(l, start, end - 1)
            # 更新start，去找下一个单词
            start = end + 1
            end += 1


ss = "a good   example"
print(Solution().reverseWords(ss))
