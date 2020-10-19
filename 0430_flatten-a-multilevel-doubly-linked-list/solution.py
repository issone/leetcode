class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        pseudoHead = Node(0, None, head, None)
        prev = pseudoHead
        stack = []
        stack.append(head)
        while stack:
            cur = stack.pop()
            prev.next = cur
            cur.prev = prev
            if cur.next:
                stack.append(cur.next)
            if cur.child:
                stack.append(cur.child)
                cur.child = None
            prev = cur
        pseudoHead.next.prev = None  # 将pseudoHead从链表中移除
        return pseudoHead.next


class Solution2:
    def flatten(self, head: Node) -> Node:
        if not head:
            return head
        pesudoHead = Node(0, None, head, None)
        self.flatten_dfs(pesudoHead, head)
        pesudoHead.next.prev = None
        return pesudoHead.next

    def flatten_dfs(self, prev, cur):
        if not cur:
            return prev

        cur.prev = prev
        prev.next = cur
        tmp = cur.next
        tail = self.flatten_dfs(cur, cur.child)
        cur.child = None
        return self.flatten_dfs(tail, tmp)
