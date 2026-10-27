# 852. Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Pattern : binary search on a condition (compare arr[m] with its neighbours)
# Time    : O(log n)  Space: O(1)
# Solved  : 2026-10-26


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
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l, r = 1, len(arr) - 2                     # the peak is never at either end, so m-1 / m+1 are valid
        while l <= r:
            m = (l + r) // 2
            if arr[m] > arr[m - 1] and arr[m] > arr[m + 1]:
                return m
            elif arr[m + 1] > arr[m]:              # still climbing: peak is to the right
                l = m + 1
            else:                                  # going down: peak is to the left
                r = m - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    check(s.peakIndexInMountainArray([0, 1, 0]), 1)
    check(s.peakIndexInMountainArray([0, 2, 1, 0]), 1)
    check(s.peakIndexInMountainArray([0, 10, 5, 2]), 1)
    check(s.peakIndexInMountainArray([3, 5, 3, 2, 0]), 1)
    check(s.peakIndexInMountainArray([1, 3, 5, 4, 2]), 2)
    check(s.peakIndexInMountainArray([0, 1, 2, 3, 2, 1, 0]), 3)
    summary()
