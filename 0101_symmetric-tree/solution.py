class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    递归的终止情况与返回值：（1）左右子树都为空 → True （2）左右子树一个为空 → False
                        （3）左右子树都不空，但是值不相等 → False （4）若上述情况都不满足， 检查 左左&右右， 左右&右左
    假设树上一共 n个节点。

    时间复杂度：这里遍历了这棵树，渐进时间复杂度为 O(n)。
    空间复杂度：这里的空间复杂度和递归使用的栈空间有关，这里递归层数不超过 nn，故渐进空间复杂度为 O(n)。

    """

    def isSymmetric(self, root: TreeNode) -> bool:
        def check(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return left.val == right.val and check(left.left, right.right) and check(right.left, left.right)

        return check(root, root)
