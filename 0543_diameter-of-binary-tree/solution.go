package _543_diameter_of_binary_tree

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func diameterOfBinaryTree(root *TreeNode) int {
	ans:=0
	var depth func(node *TreeNode) int
	depth = func(node *TreeNode) int {
		if node  == nil {
			return 0
		}
		l := depth(node.Left)
		r := depth(node.Right)
		ans = max(ans, l+r+1)
		return max(l, r) + 1
	}

	depth(root)
	return ans-1
}


func max( a, b int) int{
	if a > b{
		return a
	}
	return b
}