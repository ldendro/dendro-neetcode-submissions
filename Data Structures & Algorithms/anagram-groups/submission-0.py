class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs[0]) == "":
            return [[""]]
        mapping = {}
        res = []
        for word in strs:
            sortedText = ''.join(sorted(word))
            if sortedText in mapping:
                mapping[sortedText].append(word)
            else:
                mapping[sortedText] = [word]

        return list(mapping.values())
        