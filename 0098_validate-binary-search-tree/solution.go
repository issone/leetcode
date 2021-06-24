package _098_validate_binary_search_tree

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
二叉搜索数，中序遍历的结果是，从小到大排序的，如果后一个节点的值比前一个节点的值小则不是二叉搜索树，使用栈来模拟中序遍历过程
*/
func isValidBST(root *TreeNode) bool {
	stack := []*TreeNode{}
	pre := math.MinInt64
	for len(stack) > 0 || root != nil {
		// 先到最左下角
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		root = stack[len(stack)-1]   //栈顶元素
		stack = stack[:len(stack)-1] // 出栈
		if root.Val <= pre {
			return false
		}
		pre = root.Val
		root = root.Right
	}
	return true

}
