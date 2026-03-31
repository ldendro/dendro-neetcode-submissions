class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if word1 == '' or word2 == '':
            return word1 + word2 
        res = ''
        for i in range(len(word1)):
            res += word1[i] + word2[i]
            if i == len(word1) - 1 and i != len(word2):
                res += word2[i+1:len(word2)]
                break
            elif i == len(word2) - 1 and i != len(word1):
                res += word1[i+1:len(word1)]
                break
            
        return res