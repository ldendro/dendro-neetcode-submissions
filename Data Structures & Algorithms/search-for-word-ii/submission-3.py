class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words = set(words)
        trie = Trie(words).root
        res = set()
        seen = set()

        def dfs(r, c, curr, word):
            if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r, c) in seen or board[r][c] not in curr.children):
                return
            seen.add((r, c))
            word += board[r][c]
            curr = curr.children[board[r][c]]
            if curr.word:
                res.add(word)
            
            dfs(r-1, c, curr, word)
            dfs(r+1, c, curr, word)
            dfs(r, c-1, curr, word)
            dfs(r, c+1, curr, word)

            seen.remove((r,c))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie, "")

        return list(res)