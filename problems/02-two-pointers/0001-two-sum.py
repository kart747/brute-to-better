# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Pattern : hash map (value -> index), one pass
# Time    : O(n)      Space: O(n)
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
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}                          # value -> index
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:               # check BEFORE storing x, so [3, 3] works
                return [seen[need], i]
            seen[x] = i
        return []


if __name__ == "__main__":
    s = Solution()
    check(s.twoSum([2, 7, 11, 15], 9), [0, 1])
    check(s.twoSum([3, 2, 4], 6), [1, 2])
    check(s.twoSum([3, 3], 6), [0, 1])
    check(s.twoSum([-1, -2, -3, -4, -5], -8), [2, 4])
    summary()
