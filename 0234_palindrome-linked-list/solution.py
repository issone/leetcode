class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        时间复杂度：O(n)，其中 n 指的是链表的大小。
        空间复杂度：O(1)
        该方法的缺点是在并发环境下，函数运行时需要锁定其他线程或进程对链表的访问，因为在函数执执行过程中链表暂时断开。
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return False

        # 找到前半部分链表的尾节点
        first_half_end = self.end_of_first_half(head)
        # 转后半部分链表
        second_half_start = self.reverse_list(first_half_end.next)

        result = True
        first = head
        second = second_half_start
        while result and second:
            if first.val != second.val:
                result = False
            first = first.next
            second = second.next

        # 恢复后半部分链表
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head: ListNode):
        """找到前半部分链表的尾节点"""
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head: ListNode):
        """链表反转"""
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        时间复杂度：O(n)，其中 n 指的是链表的元素个数
        空间复杂度：O(n)，其中 n 指的是链表的元素个数
        :param head:
        :return:
        """
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]
