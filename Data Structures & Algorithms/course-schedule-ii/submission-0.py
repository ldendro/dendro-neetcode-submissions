class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()
        added = set()
        res = []

        def ordering(crs):
            if preMap[crs] == []:
                if crs not in added: 
                    added.add(crs)
                    res.append(crs)
                return True
            if crs in visit:
                return False
            visit.add(crs)
            for pre in preMap[crs]:
                if not ordering(pre):
                    return False
            visit.remove(crs)
            res.append(crs)
            added.add(crs)
            preMap[crs] = []
            return True

        for i in range(numCourses):
            if not ordering(i):
                return []
        
        return res
