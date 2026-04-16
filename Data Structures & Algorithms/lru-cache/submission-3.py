class Node:
    def __init__(self, key: int, val: int, prev: Node, next: Node):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    HASH = dict()
    CAPACITY = 0

    def __init__(self, capacity: int):
        self.HASH = dict()
        self.HASH["NEWEST"] = Node(None, None, None, None)
        self.HASH["OLDEST"] = Node(None, None, None, None)
        self.HASH["OLDEST"].next = self.HASH["NEWEST"]
        self.HASH["NEWEST"].prev = self.HASH["OLDEST"]
        self.CAPACITY = capacity

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.HASH[node.key]

    def insert(self, node: Node):
        last = self.HASH["NEWEST"].prev
        self.HASH["NEWEST"].prev = node
        node.next = self.HASH["NEWEST"]
        last.next = node
        node.prev = last

        self.HASH[node.key] = node

    def get(self, key: int) -> int:
        node = self.HASH.get(key)

        if node is None:
            return -1
        
        tmp = Node(node.key, node.val, None, None)
        self.remove(node)
        self.insert(tmp)

        return node.val
        
    def put(self, key: int, value: int) -> None:
        exist = self.HASH.get(key)

        if exist:
            self.remove(exist)
            self.insert(Node(key, value, None, None))
            return

        if len(self.HASH) == self.CAPACITY + 2:
            self.remove(self.HASH["OLDEST"].next)
            
        self.insert(Node(key, value, None, None))