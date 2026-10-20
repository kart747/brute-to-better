# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/
# Pattern : cyclic sort (home of value v is index v - 1); the leftover duplicate lands in the last slot
# Time    : O(n)      Space: O(1)
# Note    : this MODIFIES nums; the problem asks to solve it without modifying the array
#           (Floyd's cycle detection does that: tortoise/hare on i -> nums[i])
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
    def findDuplicate(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):
            ind = nums[i] - 1                      # home index of this value
            if nums[ind] != nums[i]:
                nums[ind], nums[i] = nums[i], nums[ind]   # swap it home, stay on i
            else:
                i += 1                             # already home, or a duplicate: move on
        return nums[-1]                            # n+1 slots, values 1..n: the last slot has no home


if __name__ == "__main__":
    s = Solution()
    check(s.findDuplicate([1, 3, 4, 2, 2]), 2)
    check(s.findDuplicate([3, 1, 3, 4, 2]), 3)
    check(s.findDuplicate([3, 3, 3, 3, 3]), 3)     # one value repeated many times
    check(s.findDuplicate([1, 1]), 1)
    check(s.findDuplicate([1, 1, 2]), 1)
    check(s.findDuplicate([2, 2, 2, 2, 2]), 2)
    summary()
