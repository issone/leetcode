class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode-cn.com/problems/diameter-of-binary-tree/solution/er-cha-shu-de-zhi-jing-by-leetcode-solution/
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0

        def depth(node):
            nonlocal ans
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            ans = max(ans, left + right + 1)
            return max(left, right) + 1

        depth(root)
        return ans - 1
