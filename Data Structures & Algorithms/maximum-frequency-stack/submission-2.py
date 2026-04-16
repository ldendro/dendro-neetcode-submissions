class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.maxCnt = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        self.cnt[val] = 1 + self.cnt.get(val, 0)
        if self.cnt[val] > self.maxCnt:
            self.maxCnt = self.cnt[val]
            self.stacks[self.maxCnt] = [val]
        else:
            self.stacks[self.cnt[val]].append(val)

    def pop(self) -> int:
        num = self.stacks[self.maxCnt].pop()
        self.cnt[num] -= 1
        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1
        return num


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()