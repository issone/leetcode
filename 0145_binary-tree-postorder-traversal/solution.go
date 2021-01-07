package _145_binary_tree_postorder_traversal


type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

func postorderTraversal(root *TreeNode) []int {
     var postorder func(*TreeNode)
    postorder = func(node *TreeNode) {
        if node == nil {
            return
        }
        postorder(node.Left)
        postorder(node.Right)
        res = append(res, node.Val)
    }
    postorder(root)
    return
}