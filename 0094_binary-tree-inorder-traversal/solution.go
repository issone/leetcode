package _094_binary_tree_inorder_traversal


type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

/*
迭代法
时间复杂度：O(n)，其中 n 是二叉树的节点数。二叉树的遍历中每个节点会被访问一次且只会被访问一次。
空间复杂度：O(n)，空间复杂度取决于栈深度，而栈深度在二叉树为一条链的情况下会达到 O(n) 的级别。
*/
func inorderTraversal(root *TreeNode) []int {
    var vals [] int
    var stack [] *TreeNode
    node := root
    for node != nil || len(stack) >0 {
        for node != nil {
            stack = append(stack, node)
            node = node.Left

        }

        node = stack[len(stack)-1]
        vals = append(vals, node.Val)
        stack = stack[:len(stack)-1]
        node = node.Right

    }
    return vals
}