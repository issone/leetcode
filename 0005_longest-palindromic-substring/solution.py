class Solution:
    """
    中心扩散法，从每个元素往两边扩散，直到左右两边不等
    """

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]

    def expandAroundCenter(self, s, left, right):
        """当left=right时，回文中心是一个字符，回文串的长度是奇数；
           当right=left+1时，回文中心是二个字符，回文串的长度是偶数；
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 终止时，说明，left和right之间的才是回文
        return left + 1, right - 1
