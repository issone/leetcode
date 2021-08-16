package print_link_from_end_to_start

type ListNode struct {
	Val  int
	Next *ListNode
}

// 时间复杂度和空间复杂度为O(n)
func reversePrint(head *ListNode) []int {
	if head == nil {
		return []int{}
	}

	count := 0
	p1 := head
	p2 := head
	for p1 != nil {
		count += 1
		p1 = p1.Next
	}
	res := make([]int, count)
	for i:=0;i<count;i++{
		res[count-i-1] = p2.Val
		p2 = p2.Next
	}
	return res
}
