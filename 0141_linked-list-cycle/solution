package _141_linked_list_cycle


type ListNode struct {
    Val int
    Next *ListNode
}

func hasCycle1(head *ListNode) bool {
    fast := head
    slow := head
    for fast != nil && fast.Next != nil {
        fast = fast.Next.Next
        slow = slow.Next
        if fast == slow {
            return true
        }
    }
    return false

}

func hasCycle2(head *ListNode) bool {
    node_map := make(map[*ListNode]int)

    for head != nil{
        if _, ok := node_map[head]; ok {
            return true
        }
        node_map[head] = 1
        head = head.Next
    }
    return false

}