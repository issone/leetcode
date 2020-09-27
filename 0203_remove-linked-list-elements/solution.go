package _203_remove_linked_list_elements

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeElements(head *ListNode, val int) *ListNode {
    for head != nil && head.Val == val {
        head = head.Next
    }
    p := head
    for p != nil && p.Next != nil {
        if p.Next.Val == val {
            p.Next = p.Next.Next
        } else {
            p = p.Next
        }
    }
    return head
}

