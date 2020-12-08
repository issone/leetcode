class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """利用双向链表+哈希表, 每次查询或插入时，若存在，则通过哈希表定位到节点在双向链表中的位置，并将其移动到双向链表的头部"""

    def __init__(self, capacity: int):
        self.cache = dict()  # {key: node}
        self.capacity = capacity
        self.head = DLinkedNode()  # 伪头结点
        self.tail = DLinkedNode()  # 伪尾结点
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # key存在，更新value, 并移动到头部
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = DLinkedNode(key=key, value=value)

            if self.size == self.capacity:  # 达到容量上限
                old_node = self.remove_tail()  # 移除最近最少使用的,即链尾
                self.cache.pop(old_node.key)
            else:
                self.size += 1
            self.add_to_head(node)
        self.cache[key] = node

    def remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def add_to_head(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node
