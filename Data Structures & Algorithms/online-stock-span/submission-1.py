class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        idx = len(self.arr) - 1
        while idx >= 0 and price >= self.arr[idx]:
            idx -= 1
        self.arr.append(price)
        return len(self.arr) - 1 - idx


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)