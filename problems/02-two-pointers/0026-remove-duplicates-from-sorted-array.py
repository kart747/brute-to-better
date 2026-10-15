# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Pattern : two pointers (reader + writer), in place
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
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:                       # empty list: 0 unique values
            return 0
        i = 1                              # reader
        j = 1                              # writer: next slot for a new unique value
        while i < len(nums):
            if nums[i - 1] != nums[i]:     # sorted, so a change means a new value
                nums[j] = nums[i]
                j += 1
            i += 1
        return j


def run(nums):
    """LeetCode only looks at the first k slots, so compare nums[:k] and k."""
    k = Solution().removeDuplicates(nums)
    return k, nums[:k]


if __name__ == "__main__":
    check(run([1, 1, 2]), (2, [1, 2]))
    check(run([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), (5, [0, 1, 2, 3, 4]))
    check(run([1]), (1, [1]))
    check(run([]), (0, []))
    check(run([2, 2, 2, 2]), (1, [2]))
    check(run([1, 2, 3]), (3, [1, 2, 3]))
    summary()
