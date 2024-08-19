# 2024-08-18
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courseMap = {}
        for i in range(numCourses):
            courseMap[i] = []
        for course, pre in prerequisites:
            courseMap[course].append(pre)

        def dfs(course, visited=set()):
            if course in visited:
                return False

            if not courseMap[course]:
                return True

            visited.add(course)
            for p in courseMap[course]:
                if not dfs(p, visited):
                    return False
            visited.remove(course)
            courseMap[course] = []

            return True


        result = True
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True