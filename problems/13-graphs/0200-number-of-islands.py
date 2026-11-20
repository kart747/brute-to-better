# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Pattern : grid traversal (BFS flood fill with a visited set, count connected components)
# Time    : O(R * C)      Space: O(R * C)
# Solved  : 2026-11-20
# Note    : BFS (iterative) on purpose: recursive DFS raises RecursionError on ~300x300 all-land grids.

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
    def numIslands(self, grid: list[list[str]]) -> int:
        # "1" = land, "0" = water. Connected up/down/left/right = same island.
        n = len(grid)
        m = len(grid[0])
        visited = set()                    # holds (row, col) tuples
        count = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(r, c):
            visited.add((r, c))                # mark the start cell
            q = deque([(r, c)])                # ONE item: the (row, col) pair
            while q:
                cr, cc = q.popleft()
                for dr, dc in dirs:            # for every popped cell, look at its 4 neighbors
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))  # mark when you ADD it to the queue
                        q.append((nr, nc))

        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1                 # new island found
                    bfs(r, c)                  # mark the whole island

        return count


if __name__ == "__main__":
    s = Solution()
    # each call gets a fresh grid, in case your solution changes it
    check(s.numIslands([["1", "1", "1", "1", "0"],
                        ["1", "1", "0", "1", "0"],
                        ["1", "1", "0", "0", "0"],
                        ["0", "0", "0", "0", "0"]]), 1)
    check(s.numIslands([["1", "1", "0", "0", "0"],
                        ["1", "1", "0", "0", "0"],
                        ["0", "0", "1", "0", "0"],
                        ["0", "0", "0", "1", "1"]]), 3)
    check(s.numIslands([["0"]]), 0)                    # all water
    check(s.numIslands([["1"]]), 1)                    # single cell island
    check(s.numIslands([["1", "0", "1"]]), 2)          # single row, separated
    check(s.numIslands([["1"], ["0"], ["1"], ["1"]]), 2)  # single column
    summary()
