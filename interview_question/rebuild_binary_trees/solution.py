from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
        # Output: [3,9,20,null,null,15,7]

        # 中序遍历能知道左右子树的数量和布局，前序遍历能知道左右子树的根节点
        # 1. 先遍历中序的结果，存储值及索引的关系, 后面根据前序的值，得到根节点在中序中的位置，其左边是左子树的右节点，右边是右子树的左节点
        # 2. 如何得到左子树的根节点，以及右子树的根节点呢？
        #   前序遍历根节点的下一个节点就是左子树的根节点，  右子树的根节点（用中序遍历中根节点位置-左边界的位置即为左子树长度，在前序遍历中根节点的位置+这个值即得到左子树最的右边界，+1则是右边界的根节点）
        dic = {}
        for i, val in enumerate(inorder):
            dic[val] = i

        def recur(root, left, right) -> TreeNode:
            """
            root : 当前子树的根节点的位置 (前序遍历)
            left 左边界索引位置
            right 由边界索引位置
            """
            if left > right:
                return

            node = TreeNode(preorder[root])
            node_index = dic[preorder[root]]    # 根节点在中序遍历中的位置， 前面一个就是左子树的右区间，后面一个就是右子树的左区域
            node.left = recur(root+1, left, node_index-1)
            node.right = recur(node_index-left + root + 1, node_index+1, right)
            return node

        return recur(0, 0, len(preorder) - 1)
