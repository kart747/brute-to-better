# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/
# Pattern : prefix product + suffix product (reset on 0)
#           alt: Kadane variant tracking best AND worst product ending here
# Time    : O(n)      Space: O(1)
# Solved  : 2026-10-18


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
    def maxProduct(self, nums: list[int]) -> int:
        best = nums[0]
        p = 1                              # running product from the left
        for e in nums:
            p *= e
            best = max(best, p)
            if p == 0:                     # a zero kills the product: start a fresh chunk
                p = 1
        q = 1                              # running product from the right
        for e in reversed(nums):
            q *= e
            best = max(best, q)
            if q == 0:
                q = 1
        return best


if __name__ == "__main__":
    s = Solution()
    check(s.maxProduct([2, 3, -2, 4]), 6)
    check(s.maxProduct([-2, 0, -1]), 0)
    check(s.maxProduct([-2]), -2)
    check(s.maxProduct([-2, 3, -4]), 24)              # two negatives make a positive
    check(s.maxProduct([0, 2]), 2)
    check(s.maxProduct([2, -5, -2, -4, 3]), 24)       # best subarray starts in the middle
    summary()
