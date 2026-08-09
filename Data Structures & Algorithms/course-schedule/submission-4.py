class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preHash = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preHash[course].append(prereq)

        seen = set()

        def isCycle(crs):
            if preHash[crs] == []:
                return True
            if crs in seen:
                return False
            seen.add(crs)
            for pre in preHash[crs]:
                if not isCycle(pre):
                    return False
            seen.remove(crs)
            preHash[crs] = []
            return True

        for i in range(numCourses):
            if not isCycle(i):
                return False

        return True  