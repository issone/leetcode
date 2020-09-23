package _019_remove_nth_node_from_end_of_list

type ListNode struct {
     Val int
     Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
    node:=&ListNode{0,head}
    prev,pn:=node,node
    for i:=1;i<=n+1;i++{
        pn=pn.Next
    }
    for pn!=nil {
        prev=prev.Next
        pn=pn.Next
    }
    prev.Next=prev.Next.Next
    return node.Next
}

