class Node:
    def __init__(self, val, prev=None, nxt = None):
        self.val = val
        self.prev = prev
        self.next = nxt

class LinkedList:
    def __init__(self):
        self.map = {}
        self.left = Node(0)
        self.right = Node(0, self.left)
        self.left.next = self.right

    def length(self):
        return len(self.map)

    def pushRight(self, val):
        node = Node(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node

    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            prev, nxt = node.prev, node.next
            nxt.prev, prev.next = prev, nxt
            self.map.pop(val, None)

    def popLeft(self):
        pop = self.left.next.val
        self.pop(pop)
        return pop

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.least = 1
        self.valMap = {}
        self.countMap = defaultdict(int)
        self.listMap = defaultdict(LinkedList)

    def counter(self, key):
        cnt = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt+1].pushRight(key)

        if cnt == self.least and self.listMap[cnt].length() == 0:
            self.least += 1

    def get(self, key: int) -> int:
        if key in self.valMap:
            self.counter(key)
            return self.valMap[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key not in self.valMap and len(self.valMap) == self.cap:
            res = self.listMap[self.least].popLeft()
            self.valMap.pop(res)
            self.countMap.pop(res)

        self.valMap[key] = value
        self.counter(key)
        self.least = min(self.countMap[key], self.least)
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)