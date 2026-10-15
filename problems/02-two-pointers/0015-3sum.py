# 15. 3Sum
# https://leetcode.com/problems/3sum/
# Pattern : sort + fix one number + two pointers (LC 167 inside a loop)
# Time    : O(n^2)    Space: O(1) extra (ignoring the output / sort)
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


def normalize(triplets):
    """Order of triplets (and inside each) doesn't matter, so compare sorted."""
    return sorted(sorted(t) for t in triplets)


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:                        # sorted: nothing after can sum to 0
                break
            if i > 0 and nums[i] == nums[i - 1]:   # same first number as last time
                continue
            l, r = i + 1, n - 1
            target = -nums[i]
            while l < r:
                t = nums[l] + nums[r]
                if t == target:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip equal values so the same triplet isn't recorded again
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif t < target:
                    l += 1
                else:
                    r -= 1
        return ans


if __name__ == "__main__":
    s = Solution()
    check(normalize(s.threeSum([-1, 0, 1, 2, -1, -4])), [[-1, -1, 2], [-1, 0, 1]])
    check(normalize(s.threeSum([0, 1, 1])), [])
    check(normalize(s.threeSum([0, 0, 0])), [[0, 0, 0]])
    check(normalize(s.threeSum([0, 0, 0, 0, 0])), [[0, 0, 0]])         # duplicates of one triplet
    check(normalize(s.threeSum([-2, 0, 0, 2, 2])), [[-2, 0, 2]])       # left and right dup skips
    check(normalize(s.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6])),
          [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]])
    summary()
