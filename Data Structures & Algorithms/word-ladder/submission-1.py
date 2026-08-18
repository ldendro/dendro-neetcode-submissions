class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordMap = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                temp = word[:i] + "_" + word[i+1:]
                wordMap[temp].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        count = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for j in range(len(word)):
                    temp = word[:j] + "_" + word[j+1:]
                    for newWord in wordMap[temp]:
                        if newWord not in visit:
                            visit.add(newWord)
                            q.append(newWord)

            count += 1
        return 0
