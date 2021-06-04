package _617_merge_two_binary_trees


type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

//时间复杂度：O(N)
//空间复杂度：O(h)，h 是树的高度

func mergeTrees(root1 *TreeNode, root2 *TreeNode) *TreeNode {
	if root1 == nil {
		return root2
	}
	if root2 == nil{
		return root1
	}
	root := TreeNode{Val: root1.Val+root2.Val}
	root.Left = mergeTrees(root1.Left, root2.Left)
	root.Right = mergeTrees(root1.Right, root2.Right)
	return &root
}