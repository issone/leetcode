

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
        时间复杂度：O(N)
        空间复杂度：O(N)，对于满二叉树时，要保存所有的叶子节点，即 N/2 个节点。
        """
        # 如果 t1和t2中，只要有一个是null，函数就直接返回
        if not root1:
            return root2
        if not root2:
            return root1
        queue = [(root1, root2)]
        while queue:
            r1, r2 = queue.pop(0)
            r1.val += r2.val
            # 如果r1和r2的左子树都不为空，就放到队列中
            # 如果r1的左子树为空，就把r2的左子树挂到r1的左子树上
            if r1.left and r2.left:
                queue.append((r1.left, r2.left))
            elif not r1.left:
                r1.left = r2.left
            # 对于右子树也是一样的
            if r1.right and r2.right:
                queue.append((r1.right, r2.right))
            elif not r1.right:
                r1.right = r2.right
        return root1
