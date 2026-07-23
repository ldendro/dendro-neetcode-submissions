class PrefixTree:

    def __init__(self):
        self.prefixSet = set()
        self.wordSet = set()        

    def insert(self, word: str) -> None:
        self.wordSet.add(word)
        for i in range(len(word)):
            self.prefixSet.add(word[:i])
        self.prefixSet.add(word)

    def search(self, word: str) -> bool:
        return word in self.wordSet

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefixSet
        