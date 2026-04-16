class FreqStack:

    def __init__(self):
        self.stack = []
        self.counter = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.counter[val] = 1 + self.counter.get(val, 0)

    def pop(self) -> int:
        maxFreq = 0
        pool = set()
        for key in self.counter:
            if maxFreq == self.counter[key]:
                pool.add(key)
            elif self.counter[key] > maxFreq:
                maxFreq = self.counter[key]
                pool = set()
                pool.add(key)

        for i in range(len(self.stack)-1,-1,-1):
            num = self.stack[i]
            if num in pool:
                self.counter[num] -= 1
                del self.stack[i]
                return num


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()