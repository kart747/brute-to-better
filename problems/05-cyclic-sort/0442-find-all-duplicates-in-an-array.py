# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Pattern : cyclic sort (home of value v is index v - 1); a value left in the wrong slot is a duplicate
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
    def findDuplicates(self, nums: list[int]) -> list[int]:
        i = 0
        while i < len(nums):
            ind = nums[i] - 1                      # home index of this value
            if nums[ind] != nums[i]:
                nums[i], nums[ind] = nums[ind], nums[i]   # swap it home, stay on i
            else:
                i += 1                             # already home, or a duplicate: move on
        ans = []
        for i, x in enumerate(nums):
            if i + 1 != x:                         # x could not take its home slot: it appears twice
                ans.append(x)
        return ans


def run(nums):
    """Order of the answer doesn't matter, so compare sorted."""
    return sorted(Solution().findDuplicates(nums))


if __name__ == "__main__":
    check(run([4, 3, 2, 7, 8, 2, 3, 1]), [2, 3])
    check(run([1, 1, 2]), [1])
    check(run([1]), [])
    check(run([1, 2, 3]), [])
    check(run([2, 1, 2, 1]), [1, 2])
    check(run([3, 3, 1, 1, 2, 2]), [1, 2, 3])
    summary()
