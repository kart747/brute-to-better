# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Pattern : two pointers, always move the shorter wall
# Time    : O(n)      Space: O(1)
# Solved  : 2026-10-15


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
    def maxArea(self, height: list[int]) -> int:
        best = 0
        i, j = 0, len(height) - 1
        while i < j:
            best = max(best, min(height[i], height[j]) * (j - i))
            # width only shrinks, so the only way to improve is a taller shorter wall:
            # moving the taller side can never help, move the shorter one
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return best


if __name__ == "__main__":
    s = Solution()
    check(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
    check(s.maxArea([1, 1]), 1)
    check(s.maxArea([4, 3, 2, 1, 4]), 16)
    check(s.maxArea([1, 2, 1]), 2)
    summary()
