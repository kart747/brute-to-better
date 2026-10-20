# 448. Find All Numbers Disappeared in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Pattern : cyclic sort (home of value v is index v - 1), duplicates stay out of place
# Time    : O(n)      Space: O(1) extra (output not counted)
# Solved  : 2026-10-20


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
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        i = 0
        while i < len(nums):
            ind = nums[i] - 1                      # home index of this value
            if ind < len(nums) and nums[ind] != nums[i]:
                nums[i], nums[ind] = nums[ind], nums[i]   # swap it home, stay on i
            else:
                i += 1                             # already home, or a duplicate: move on
        ans = []
        for i, x in enumerate(nums):
            if x - 1 != i:                         # index i holds the wrong number...
                ans.append(i + 1)                  # ...so the number i + 1 is missing
        return ans


if __name__ == "__main__":
    s = Solution()
    check(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]), [5, 6])
    check(s.findDisappearedNumbers([1, 1]), [2])
    check(s.findDisappearedNumbers([1, 2, 3]), [])
    check(s.findDisappearedNumbers([2, 2]), [1])
    check(s.findDisappearedNumbers([1]), [])
    check(s.findDisappearedNumbers([3, 3, 3]), [1, 2])
    summary()
