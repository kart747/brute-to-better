# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/
# Pattern : counting sort (3 distinct values), two passes, in place
#           follow-up: one pass with three pointers (Dutch national flag)
# Time    : O(n)      Space: O(1)
# Solved  : 2026-10-16


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
    def sortColors(self, nums: list[int]) -> None:
        """Sort in place: all 0s, then 1s, then 2s. Don't return anything."""
        a, b = 0, 0                        # a = count of 0s, b = count of 1s
        for x in nums:
            if x == 0:
                a += 1
            elif x == 1:
                b += 1
        for i in range(a):                 # slots [0, a)      -> 0
            nums[i] = 0
        for i in range(a, a + b):          # slots [a, a + b)  -> 1
            nums[i] = 1
        for i in range(a + b, len(nums)):  # the rest          -> 2
            nums[i] = 2


def run(nums):
    Solution().sortColors(nums)
    return nums


if __name__ == "__main__":
    check(run([2, 0, 2, 1, 1, 0]), [0, 0, 1, 1, 2, 2])
    check(run([2, 0, 1]), [0, 1, 2])
    check(run([0]), [0])
    check(run([1, 2, 0]), [0, 1, 2])
    check(run([2, 2, 2]), [2, 2, 2])
    check(run([1, 1, 0, 0, 2, 2, 1, 0]), [0, 0, 0, 1, 1, 1, 2, 2])
    summary()
