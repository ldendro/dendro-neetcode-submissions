class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderCount = {}
        for i in range(len(order)):
            orderCount[order[i]] = i

        def dfs(i):
            if i + 1 >= len(words):
                return True

            word1, word2 = words[i], words[i+1]

            for j in range(len(word1)):
                if j >= len(word2) or orderCount[word1[j]] > orderCount[word2[j]]:
                    return False
                if orderCount[word1[j]] < orderCount[word2[j]]:
                    break

            return dfs(i + 1)

        return dfs(0)
                