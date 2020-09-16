# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        当一个列表比另一个列表长时
        当一个列表为空时，即出现空列表
        求和运算最后可能出现额外的进位，这一点很容易被遗忘

        为了处理方法统一，可以先建立一个虚拟头结点，这个虚拟头结点的 Next 指向真正的 head，这样 head 不需要单独处理，直接 while 循环即可。
        另外判断循环终止的条件不用是 p.Next ！= nil，这样最后一位还需要额外计算，循环终止条件应该是 p != nil。
        :param l1:
        :param l2:
        :return:
        """
        temp = ListNode(0)
        l = temp
        carry = 0
        while l1 or l2:
            val1, l1 = (l1.val, l1.next) if l1 else (0, None)
            val2, l2 = (l2.val, l2.next) if l2 else (0, None)
            l.next = ListNode((carry + val1 + val2) % 10)
            l = l.next
            carry = (carry + val1 + val2) // 10
        if carry > 0:
            l.next = ListNode(carry)
        return l.next
