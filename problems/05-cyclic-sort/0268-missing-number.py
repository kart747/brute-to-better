# 268. Missing Number
# https://leetcode.com/problems/missing-number/
# Pattern : cyclic sort (put each value at its home index), alt: sum / XOR
# Time    : O(n)      Space: O(1)
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
    def missingNumber(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):
            ind = nums[i]                  # home index of this value (values are 0..n)
            # value n has no home; stop when the right value is already at its home
            while ind < len(nums) and nums[i] != nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                ind = nums[i]
            i += 1
        for j in range(len(nums)):
            if nums[j] != j:
                return j                   # index j is the missing number
        return len(nums)                   # every index 0..n-1 was correct, so n is missing


if __name__ == "__main__":
    s = Solution()
    check(s.missingNumber([3, 0, 1]), 2)
    check(s.missingNumber([0, 1]), 2)
    check(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)
    check(s.missingNumber([0]), 1)
    check(s.missingNumber([1]), 0)
    check(s.missingNumber([0, 1, 2]), 3)
    summary()
