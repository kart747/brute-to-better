# 841. Keys and Rooms
# https://leetcode.com/problems/keys-and-rooms/
# Pattern : graph traversal (DFS/BFS from room 0, check everything was reached)
# Time    : O(V + E)      Space: O(V)
# Solved  : 2026-11-18

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
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        # rooms[i] = the keys found in room i. A key = the number of a room it opens.
        # Room 0 is unlocked at the start. rooms IS already an adjacency list.
        visited = [False] * len(rooms)

        def dfs(node):
            visited[node] = True
            for nei in rooms[node]:
                if not visited[nei]:
                    dfs(nei)

        dfs(0)
        return all(visited)



if __name__ == "__main__":
    s = Solution()
    check(s.canVisitAllRooms([[1], [2], [3], []]), True)
    check(s.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]), False)   # room 2 unreachable
    check(s.canVisitAllRooms([[]]), True)                              # only room 0
    check(s.canVisitAllRooms([[2], [], [1]]), True)                    # 0 -> 2 -> 1
    check(s.canVisitAllRooms([[], []]), False)                         # room 0 has no keys
    check(s.canVisitAllRooms([[1], [0], [0]]), False)                  # keys point back, room 2 never opened
    summary()
