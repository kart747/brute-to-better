# 797. All Paths From Source to Target
# https://leetcode.com/problems/all-paths-from-source-to-target/
# Pattern : DFS + backtracking on a DAG (path list: append going in, pop coming out)
# Time    : O(2^n * n)      Space: O(n) recursion + output
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
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        # graph is ALREADY an adjacency list: graph[i] = nodes you can go to from i
        n = len(graph)
        path = []        # final answer: a list of complete routes

        # No `visited` list: this is a DAG (no cycles), so a route can never
        # loop back. A visited list would block other valid routes through
        # the same node (e.g. 0->1->3 would hide 0->2->3).

        def go(node, temp):
            # temp = the route from 0 to the node we are standing on right now
            temp.append(node)                 # step INTO node

            if node == n - 1:                 # reached the target
                path.append(temp[:])          # save a COPY (snapshot of the route)
                                              # not `temp` itself, or later changes would alter it

            for nei in graph[node]:           # try every next step from here
                go(nei, temp)                 # pass the same shared list down

            temp.pop()                        # step OUT of node (undo the append)
                                              # so the next route branches from the right place

        go(0, [])                             # start at node 0 with an empty route
        return path





if __name__ == "__main__":
    s = Solution()
    # sort so the order of paths doesn't matter
    check(sorted(s.allPathsSourceTarget([[1, 2], [3], [3], []]) or []), [[0, 1, 3], [0, 2, 3]])
    check(sorted(s.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]) or []),
          [[0, 1, 2, 3, 4], [0, 1, 3, 4], [0, 1, 4], [0, 3, 4], [0, 4]])
    check(sorted(s.allPathsSourceTarget([[1], []]) or []), [[0, 1]])
    summary()
