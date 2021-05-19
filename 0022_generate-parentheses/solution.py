from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        括号数为 n，那么一个合法的括号组合，应该包含 n 个左括号和 n 个右括号，组合总长度为 2n。
        一对合法的括号，应该是先出现左括号，再出现右括号。那么意味着*任意一个右括号的左边，至少有一个左括号。
        一对合法的括号组合，最终得分必然为 0 （左括号和右括号的数量相等，假设左括号分值为1，右括号分值为-1）。
        整个 DFS 过程中，得分值范围在 [0, n]（得分不可能超过 n ，意味着不可能添加数量超过 n 的左括号；得分不可能为负数，意味着每一个右括号必然有一个左括号进行匹配）

        「成对匹配」相关的题型都能转化为「分值有效性」的数学判定
        """
        res = []  # 结果集

        def dfs(cur_index, cur_score, cur_str, max_length=2 * n, max_score=n):
            """
            cur_index: 当前遍历的位置
            cur_score: 当前得分， 令 '(' 为 1， ')' 为 -1
            cur_str: 当前拼接结果
            max_length: 字符总长度
            max_score: 最大分值
            """
            if cur_index == max_length:  # 到达最大长度则停止递归，保存结果
                if cur_score == 0:  # 保存结果前需要校验合法性
                    res.append(cur_str)
            else:
                if cur_score + 1 <= max_score:
                    dfs(cur_index + 1, cur_score + 1, cur_str + "(")
                if cur_score - 1 >= 0:
                    dfs(cur_index + 1, cur_score - 1, cur_str + ")")

        dfs(0, 0, "", 2 * n, n)
        return res
