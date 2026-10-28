# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Pattern : binary search (find the pivot with nums[m] > nums[r], then plain binary search on a sorted half)
# Time    : O(log n)  Space: O(1)
# Solved  : 2026-10-28


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
    def bs(self, nums, target, l, r):
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:                               # find the index of the smallest element (the pivot)
            m = (l + r) // 2
            if nums[m] > nums[r]:                  # the drop is to the right of m
                l = m + 1
            else:                                  # the drop is at m or to its left
                r = m
        p = l

        ans = self.bs(nums, target, 0, p - 1)      # left sorted half (empty if not rotated)
        if ans != -1:
            return ans
        return self.bs(nums, target, p, len(nums) - 1)    # right sorted half


if __name__ == "__main__":
    s = Solution()
    check(s.search([4, 5, 6, 7, 0, 1, 2], 0), 4)
    check(s.search([4, 5, 6, 7, 0, 1, 2], 3), -1)
    check(s.search([1], 0), -1)
    check(s.search([1], 1), 0)
    check(s.search([1, 3], 3), 1)                  # not rotated
    check(s.search([3, 1], 1), 1)                  # two elements, rotated
    check(s.search([3, 1], 3), 0)
    check(s.search([5, 1, 3], 5), 0)               # target at the front of the left half
    check(s.search([6, 7, 0, 1, 2, 4, 5], 7), 1)
    summary()
