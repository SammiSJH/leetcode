# 2024-8-20

# DFS: TLE
class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(n):
            if n == 0:
                return 1
            elif n < 0:
                return 0

            result = 0
            for i in [1, 2]:
                result += dfs(n-i)

            return result

        return dfs(n)

# TLE
class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2

            return dfs(n-1) + dfs(n-2)

        return dfs(n)


# Accepted
# DP
class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}
        cache[1] = 1
        cache[2] = 2

        def dfs(n):
            if n in cache:
                return cache[n]

            cache[n] = dfs(n-1) + dfs(n-2)

            return cache[n]

        return dfs(n)