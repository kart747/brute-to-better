# 918. Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/
# Pattern : Kadane variant (best of: normal max, or total - min subarray)
# Time    : O(n)      Space: O(1)
# Solved  : 2026-10-19


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
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        cur_max = best_max = nums[0]       # best subarray ending here / overall (maximum)
        cur_min = best_min = nums[0]       # same, for the minimum
        total = nums[0]
        for x in nums[1:]:
            cur_max = max(cur_max + x, x)  # continue the previous subarray, or start fresh at x
            best_max = max(best_max, cur_max)
            cur_min = min(cur_min + x, x)
            best_min = min(best_min, cur_min)
            total += x
        if best_max < 0:                   # every number is negative: wrapping would mean "take nothing"
            return best_max
        return max(best_max, total - best_min)   # no wrap, or wrap = total minus the smallest middle chunk


if __name__ == "__main__":
    s = Solution()
    check(s.maxSubarraySumCircular([1, -2, 3, -2]), 3)
    check(s.maxSubarraySumCircular([5, -3, 5]), 10)          # wraps around the end
    check(s.maxSubarraySumCircular([-3, -2, -3]), -2)        # all negative
    check(s.maxSubarraySumCircular([3, -1, 2, -1]), 4)
    check(s.maxSubarraySumCircular([3, -2, 2, -3]), 3)
    check(s.maxSubarraySumCircular([-2]), -2)
    summary()
