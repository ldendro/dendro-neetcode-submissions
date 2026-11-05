class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0] * 3
        for triplet in triplets:
            temp = [0] * 3
            for i in range(3):
                if triplet[i] > target[i]:
                    break
                temp[i] = max(res[i], triplet[i])
            if temp[-1] != 0:
                res = temp
        
        return res == target