class Solution:
    def numTrees(self, n: int) -> int:
        store = [1, 1]  # f(0),f(1)
        if n <= 1:
            return store[n]
        for m in range(2, n + 1):
            s = m - 1
            count = 0
            for i in range(m):
                count += store[i] * store[s - i]
            store.append(count)
        return store[n]

# https://leetcode-cn.com/problems/unique-binary-search-trees/solution/er-cha-sou-suo-shu-fu-xi-li-zi-jie-shi-si-lu-by-xi/
