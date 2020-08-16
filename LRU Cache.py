# double linkedlist with dict in python 3
class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None
		
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next =self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1 
        else:
            node = self.map[key]
            self.move_to_head(node)
            return node.value
    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev 
    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next 
        self.head.next.prev = node
        self.head.next = node
    
    
    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            node = Node(key, value)
            self.map[key] = node
            self.add_to_head(node)
            self.size += 1
            if self.size > self.cap:
                removed = self.remove_tail()
                self.map.pop(removed.key)
                self.size -= 1 
        else:
            node = self.map[key]
            node.value = value
            self.move_to_head(node)
    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node
