class LRCUcache:
    def __init__(self, maxsize):
        self.double_list = DoubleLinkedList()
        self.max_size = maxsize
        self.key_to_node = {}
        self.size = 0

    def get(self, key):
        if key in self.key_to_node:
            node = self.key_to_node[key]
            ret_val = node.value

            if self.double_list.head.next != node:
                self.double_list.unlink_node(node)
                self.double_list.add_to_front(node)

            return ret_val

    def put(self, key, value):
        node = None

        if key not in self.key_to_node:
            #add it

            node = Node(key, value)
            self.key_to_node[key] = node
            self.size += 1

        else:
            node = self.key_to_node[key]
            node.value = value
            self.double_list.unlink_node(node)
        self.double_list.add_to_front(node)

        # Do we need to kick items out of LRU?

        if self.size > self.max_size:
            lru_node = self.double_list.tail.prev
            self.key_to_node.pop(lru_node.key)
            self.double_list.unlink_node(lru_node)
            self.size -= 1

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.head.next = self.head
        self.head.prev = self.tail


    def unlink_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node






