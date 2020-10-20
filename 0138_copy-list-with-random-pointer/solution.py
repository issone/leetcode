class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """时间复杂度：O(N),空间复杂度：O(1)"""
        if not head:
            return head
        ptr = head
        while ptr:  # 使原链表每个节点后都跟上原节点的复制节点  将 a -> b -> c 的链表变成 a -> a' -> b -> b' -> c -> c'
            new_node = Node(ptr.val, ptr.next)
            ptr.next = new_node
            ptr = new_node.next

        ptr = head
        while ptr:  # 给新的节点设置random
            # 假如 a -> random存在，则 'a' -> random 一定等于 a -> random -> next

            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        old_list_head = head
        new_list_head = head.next
        head_new = head.next

        while old_list_head:  # 将新的链表中原链表中分离
            old_list_head.next = old_list_head.next.next
            new_list_head.next = new_list_head.next.next if new_list_head.next else None
            old_list_head = old_list_head.next
            new_list_head = new_list_head.next
        return head_new
