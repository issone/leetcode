package _061_rotate_list


type ListNode struct {
    Val int
    Next *ListNode
}

func rotateRight(head *ListNode, k int) *ListNode {
    if head == nil || head.Next == nil || k == 0 {
        return head
    }
    curr := head
    length := 1
    for curr.Next != nil {
        length++
        curr = curr.Next
    }

    // 成环
    curr.Next = head

    curr = head
    for i := 1; i < (length - k%length); i++ {
        curr = curr.Next
    }
    // 此时 curr是新的链尾， curr的下一个节点是新的链头
    result := curr.Next
    curr.Next = nil
    return result
}
