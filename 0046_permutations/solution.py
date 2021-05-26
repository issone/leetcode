from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        如果nums = [1, 2, 3]
        其全排列有: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
        该题适合用DFS之回溯法求解从树的根节点[]开始按照深度逐个遍历
        回溯法算需要时刻关注两大变量：
            (1) 递归的终止条件(回溯的本质是递归)
            (1) 回溯过程中某时间点的当前状态
        
        下面首先对必要变量进行初始化
        depth: 当前所在位置所处树的深度
        path: 记录当前遍历过的数字序列, i.e. [1], [1, 2], [1, 2, 3]
        res: 最后输出的包含所有的全序列的数组
        ls_used: 由于全排列同一个数字不可出现2次, 所以需创建一个额外数组
                 跟踪每一个数字的使用情况, 其初始为全False 
        '''
        depth, path, res = 0, [], []
        ls_used = [False for _ in nums]

        # 初始化所有必要变量后开始从树的根节点([])进行深度遍历
        self.dfs(nums, depth, ls_used, path, res)
        return res

    def dfs(self, nums, depth, ls_used, path, res):
        # 递归终止条件: 达到树的尾部, 则将path中存储的数字加到res中
        if depth == len(nums):
            # 这里用path[:]才能取得path里面存储的值，否则path是空值
            res.append(path[:])
            return

        # 在当前节点挨个尝试所有没有被探索过的数字
        for i, used in enumerate(ls_used):
            # 跳过已经在path中出现的数字
            if used:
                continue
            # 如果该数字没有被使用, 则添加到path中, 并将数字状态改为True表示其已经被遍历
            path.append(nums[i])
            ls_used[i] = True

            # 递归: 往下一层进一步探索
            self.dfs(nums, depth + 1, ls_used, path, res)

            # 回溯到原来位置, 把path中最后新加入的弹出, 之前使用过数字现在变成未使用
            path.pop()
            ls_used[i] = False
