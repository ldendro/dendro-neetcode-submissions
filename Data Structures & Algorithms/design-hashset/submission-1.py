class MyHashSet:

    def __init__(self):
        self.arr = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.arr.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.arr.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.arr:
            return True
        else:
            return False