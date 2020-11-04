class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """思路：
        要处理k大于n的情况，需要对k进行处理，k = k%n   n是指链表的长度
        所以需要计算链表长度
        由于k可以大于整个链表的长度，因此该链表可看做一个循环链表
        每个节点向右移动k个位置相当于将倒数第k个节点之后的节点移到头结点之前

        使用快慢指针，快指针先走k步，然后快慢指针一起走，当快指针到达链表尾部时，慢指针所在位置即新的链尾
        慢指针的下一个即新的链头

        """
        if not head or not head.next or not k:
            return head
        tmp, n = head, 0
        while tmp:
            tmp = tmp.next
            n += 1
        k %= n
        if k == 0:
            return head
        fast = slow = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        new_head = slow.next
        fast.next = head    # 成环
        slow.next = None  # 断环
        return new_head


