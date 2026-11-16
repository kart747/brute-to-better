# 1971. Find if Path Exists in Graph
# https://leetcode.com/problems/find-if-path-exists-in-graph/
# Pattern : graph traversal (BFS or DFS from source, look for destination)
# Time    : O(V + E)      Space: O(V + E)
# Solved  : 2026-11-16

from collections import deque


# ---- test helper: one PASS/FAIL line per case + a summary at the end ----
tests_run = tests_passed = 0


def check(got, expected):
    global tests_run, tests_passed
    tests_run += 1
    if got == expected:
        tests_passed += 1
        print(f"✅ PASS #{tests_run}")
    else:
        print(f"❌ FAIL #{tests_run}  got {got}, expected {expected}")


def summary():
    ok = tests_passed == tests_run
    print(f"\n{tests_passed}/{tests_run}  {'✅ ALL PASSED' if ok else '❌ SOME FAILED'}")
# -------------------------------------------------------------------------


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # build the adjacency list (undirected: add both directions)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * n

        def dfs(node: int) -> bool:
            if node == destination:
                return True
            
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    if dfs(nei):          # found it down this branch
                        return True       # pass the True back up
            return False
            


        # start the search from source
        return dfs(source)


if __name__ == "__main__":
    s = Solution()
    check(s.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2), True)
    check(s.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5), False)
    check(s.validPath(1, [], 0, 0), True)                      # source == destination
    check(s.validPath(2, [], 0, 1), False)                     # no edges
    check(s.validPath(4, [[0, 1], [1, 2], [2, 3]], 3, 0), True)  # undirected: works backwards
    check(s.validPath(4, [[0, 1], [0, 2], [2, 3]], 0, 3), True)   # first neighbor is a dead end
    summary()
