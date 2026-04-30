class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.store[key]) - 1
        arr = self.store[key]
        res = -1
        while l <= r:
            m = l + (r - l) // 2
            if arr[m][1] > timestamp:
                r = m - 1
            elif arr[m][1] < timestamp:
                l = m + 1
                res = m
            else:
                return arr[m][0]
        
        return "" if res == -1 else arr[res][0]
