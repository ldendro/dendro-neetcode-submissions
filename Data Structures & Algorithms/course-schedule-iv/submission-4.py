class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preList = [[] for i in range(numCourses)]
        isPrereq = [[-1] * numCourses for _ in range(numCourses)]
        for pre, crs in prerequisites:
            isPrereq[crs][pre] = 1
            preList[crs].append(pre)

        def dfs(crs, tgt):
            if isPrereq[crs][tgt] != -1:
                return isPrereq[crs][tgt] == 1

            for pre in preList[crs]:
                if pre == tgt or dfs(pre, tgt):
                    isPrereq[crs][tgt] = 1
                    return True
            
            isPrereq[crs][tgt] = 0
            return False

        res = []
        for pre, crs in queries:
            res.append(dfs(crs, pre))

        return res