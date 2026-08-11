class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hashMap = {i: [] for i in range(n)}
        for num1, num2 in edges:
            hashMap[num1].append(num2)
            hashMap[num2].append(num1)


        visit = set()

        def cycle(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for num in hashMap[i]:
                if prev != num:
                    if not cycle(num, i):
                        return False
            return True

        return cycle(0,0) and len(visit) == n         
