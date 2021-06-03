class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 层序遍历，广度遍历
        if root is None:
            return

        queue = [root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left or cur_node.right:
                cur_node.left, cur_node.right = cur_node.right, cur_node.left
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
        return root

