class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    """
    双指针法
     时间复杂度：O(n)，空间复杂度：O(1)，
    """

    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head

        while fast and fast.next:  # 当链表为空或者只有一个结点时，就不执行循环体里的程序，返回False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


class Solution2:
    """
    哈希表
     时间复杂度：O(1)，空间复杂度：O(n)，
    """

    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False
