package _144_binary_tree_preorder_traversal


type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

/*
迭代法
时间复杂度：O(n)，其中 n 是二叉树的节点数。每一个节点恰好被遍历一次。
空间复杂度：O(n)，为迭代过程中显式栈的开销，平均情况下为O(logn)，最坏情况下树呈现链状，为 O(n)。
*/
func preorderTraversal(root *TreeNode) []int {
    var vals [] int
    var stack [] *TreeNode
    node := root
    for node != nil || len(stack) >0 {
        for node != nil {
            vals = append(vals, node.Val)
            stack = append(stack, node)
            node = node.Left
        }
        // 当前节点的左边遍历完成，接着遍历右边的
        node = stack[len(stack)-1].Right
        stack = stack[:len(stack)-1]
    }
    return vals
}