# least node left, most node right, doubly linked list, hashmap where keyh is key and value is node
# Need update function to update the doubly linked list on both get() and put(), still O(1) because its 
# constant amount of operations, where nxt = node.next, least.next = nxt, nxt.prev = least, node.prev = most.prev, node.next = most, most.prev = node
# 
# For Get use node = hashmap[key] if key exists then update(node)
# For put use node = hahmap[key], node.val = newVal, update(node) if key exists otherwise create new node
class ListNode():
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: ListNode):
        nxt, prev = node.next, node.prev
        prev.next, nxt.prev = nxt, prev

    def insert(self, node: ListNode):
        mostRecent = self.right.prev
        node.next = self.right
        node.prev = mostRecent
        mostRecent.next = node
        self.right.prev = node 

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        self.hashmap[key] = ListNode(key, value)
        self.insert(self.hashmap[key])

        if len(self.hashmap) > self.capacity:
            node = self.left.next
            del self.hashmap[node.key]
            self.remove(node)
        


        
