class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit = set()
        cycle = set()
        res = []

        def ordering(crs):
            if crs in visit:
                return True
            if crs in cycle:
                return False
            cycle.add(crs)
            for pre in preMap[crs]:
                if not ordering(pre):
                    return False
            cycle.remove(crs)
            res.append(crs)
            visit.add(crs)
            return True

        for i in range(numCourses):
            if not ordering(i):
                return []
        
        return res
