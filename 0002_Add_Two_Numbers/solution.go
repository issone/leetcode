package _002_Add_Two_Numbers

//* Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dumyNode := &ListNode{Val: 0}
	n1, n2, carry, current := 0, 0, 0, dumyNode
	for l1 != nil || l2 != nil || carry != 0 {
		if l1 == nil {
			n1 = 0
		} else {
			l1 = l1.Next
			n1 = l1.Val

		}
		if l2 == nil {
			n2 = 0
		} else {
			n2 = l2.Val
			l2 = l2.Next
		}
		current.Next = &ListNode{Val: (n1 + n2 + carry) % 10}
		current = current.Next
		carry = (carry + n1 + n2) / 10
	}
	return dumyNode.Next
}
