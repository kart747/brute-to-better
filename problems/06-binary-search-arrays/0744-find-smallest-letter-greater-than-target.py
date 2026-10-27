# 744. Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Pattern : binary search (first index where letters[i] > target, wrap around with %)
# Time    : O(log n)  Space: O(1)
# Solved  : 2026-10-26


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
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        l, h = 0, len(letters) - 1
        while l <= h:
            m = (l + h) // 2
            if letters[m] > target:
                h = m - 1
            else:
                l = m + 1
        return letters[l % len(letters)]           # l == n means nothing is bigger: wrap to the first


if __name__ == "__main__":
    s = Solution()
    check(s.nextGreatestLetter(["c", "f", "j"], "a"), "c")
    check(s.nextGreatestLetter(["c", "f", "j"], "c"), "f")
    check(s.nextGreatestLetter(["x", "x", "y", "y"], "z"), "x")   # wraps around
    check(s.nextGreatestLetter(["c", "f", "j"], "j"), "c")        # equal to the last: wraps
    check(s.nextGreatestLetter(["a", "b"], "a"), "b")
    check(s.nextGreatestLetter(["a", "b"], "b"), "a")
    check(s.nextGreatestLetter(["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], "e"), "n")
    summary()
