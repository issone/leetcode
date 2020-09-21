package _142_linked_list_cycle_ii

type ListNode struct {
	Val  int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {
	slow := head
	fast := head
	for (fast != nil) && (fast.Next != nil) {
		fast = fast.Next.Next
		slow = slow.Next
		// 当快指针和慢指针相遇后，从head出发，head遇到slow时，head指向环入口
		if fast == slow {
			for head != slow {
				head = head.Next
				slow = slow.Next
			}
			return head
		}
	}
	return nil

}
