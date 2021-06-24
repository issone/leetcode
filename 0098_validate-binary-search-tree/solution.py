class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 递归法， 时间，空间复杂度都为O(n)
        def dfs(node: TreeNode, left, right) -> bool:
            if node is None:
                return True
            if left < node.val < right:
                return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
            return False

        return dfs(root, -float('inf'), float('inf'))
