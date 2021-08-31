class CQueue:

    def __init__(self):
        # 插入队列
        self.stack1 = []
        # 删除队列
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2:  # 这里面是stack1中倒序的结果，删除头即删除stack2的尾
            return self.stack2.pop()
        # stack2没值，且stack1没值，说明没法删除了
        if not self.stack1:
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
