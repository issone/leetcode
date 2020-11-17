package _138_copy_list_with_random_pointer

type Node struct {
    Val int
    Next *Node
    Random *Node
}


func getCloneNode(vistedMap map[*Node]*Node, p *Node) *Node{
    if v, ok := vistedMap[p]; ok {
        return v
    } else {
        var v *Node
        if p != nil {
           v = &Node{p.Val, nil, nil}
        }
        vistedMap[p] = v
        return v
    }
}

// 时间复杂度：O(N) 。因为我们需要将原链表逐一遍历。
// 空间复杂度：O(N) 。 我们需要维护一个字典，保存旧的节点和新的节点的对应。因此总共需要 N 个节点，需要 O(N)的空间复杂度。


func copyRandomList(head *Node) *Node {
    if head == nil {
        return nil
    }
    vistedMap := make(map[*Node]*Node)
    oldNode := head
    newNode := getCloneNode(vistedMap, oldNode)
    newHead := newNode
    for oldNode != nil {
         newNode.Next = getCloneNode(vistedMap, oldNode.Next)
         newNode.Random = getCloneNode(vistedMap, oldNode.Random)

         oldNode = oldNode.Next
         newNode = newNode.Next
    }
    return newHead
}
