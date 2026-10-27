# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Pattern : binary search (lower bound: first index >= target; then first index > target, minus 1)
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
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l, h = 0, len(nums) - 1
        n = len(nums)
        while l <= h:                              # first index where nums[i] >= target
            m = (l + h) // 2
            if nums[m] >= target:
                h = m - 1
            else:
                l = m + 1
        j = l
        if j >= n:
            return [-1, -1]
        if target == nums[l]:
            l, h = 0, len(nums) - 1
            while l <= h:                          # first index where nums[i] > target
                m = (l + h) // 2
                if nums[m] > target:
                    h = m - 1
                else:
                    l = m + 1
            return [j, h]                          # h ends one before that index = last occurrence
        return [-1, -1]


if __name__ == "__main__":
    s = Solution()
    check(s.searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])
    check(s.searchRange([5, 7, 7, 8, 8, 10], 6), [-1, -1])
    check(s.searchRange([], 0), [-1, -1])
    check(s.searchRange([1], 1), [0, 0])
    check(s.searchRange([2, 2], 2), [0, 1])
    check(s.searchRange([1, 2, 3], 4), [-1, -1])        # target past the end
    check(s.searchRange([1, 2, 3], 0), [-1, -1])        # target before the start
    check(s.searchRange([1, 1, 1, 2, 3], 1), [0, 2])
    summary()
