class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dict_p = {i :[] for i in range(numCourses)}
        visit = set()
        for c, p in prerequisites:
            if c not in dict_p:
                dict_p[c] = []
            dict_p[c].append(p)


        def dfs(crs):
            if crs in visit:
                return False
            if dict_p[crs] == []:
                return True

            visit.add(crs)
            for k in dict_p[crs]:
                if not dfs(k):
                    return False
            visit.remove(crs)
            dict_p[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True

