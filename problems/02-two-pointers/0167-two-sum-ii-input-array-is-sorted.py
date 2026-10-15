# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Pattern : two pointers on a sorted array
# Time    : O(n)      Space: O(1)
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
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i, j = 0, len(numbers) - 1
        while i < j:                       # stop when the pointers meet
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1, j + 1]      # 1-indexed
            if s > target:
                j -= 1                     # too big: only a smaller right value can help
            else:
                i += 1                     # too small: only a bigger left value can help
        return []


if __name__ == "__main__":
    s = Solution()
    check(s.twoSum([2, 7, 11, 15], 9), [1, 2])
    check(s.twoSum([2, 3, 4], 6), [1, 3])
    check(s.twoSum([-1, 0], -1), [1, 2])
    check(s.twoSum([1, 3, 4, 8], 11), [2, 4])
    summary()
