class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(i, j, idx, seen):
            if board[i][j] == word[idx]:
                if idx == len(word) - 1:
                    return True
                seen.add((i, j))
                if i - 1 >= 0 and (i-1, j) not in seen:
                    if search(i-1, j, idx + 1, seen):
                        return True
                if i + 1 < len(board) and (i+1, j) not in seen:
                    if search(i+1, j, idx + 1, seen):
                        return True
                if j - 1 >= 0 and (i, j-1) not in seen:
                    if search(i, j-1, idx + 1, seen):
                        return True
                if j + 1 < len(board[0]) and (i, j+1) not in seen:
                    if search(i, j+1, idx + 1, seen):
                        return True
                seen.remove((i, j))


        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(i, j, 0, set()):
                    return True
        
        return False