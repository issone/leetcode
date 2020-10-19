package _430_flatten_a_multilevel_doubly_linked_list

type Node struct {
    Val intf
    Prev *Node
    Next *Node
    Child *Node
}


func flatten(root *Node) *Node {
    cur := root
    for cur != nil {
        next := cur.Next
        if cur.Child != nil {
            child := cur.Child
            cur.Next = child
            child.Prev = cur
            cur.Child = nil
            tail := child
            for tail != nil && tail.Next != nil {
                tail=tail.Next
            }
			tail.Next = next
            if next != nil {
				next.Prev = tail
			}
        }
        cur = cur.Next
        }
    return root
}