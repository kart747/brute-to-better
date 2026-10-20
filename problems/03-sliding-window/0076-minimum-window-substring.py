# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/
# Pattern : sliding window with a "still missing" counter
# Time    : O(|s| + |t|)      Space: O(charset)
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
        print(f"❌ FAIL #{tests_run}  got {got!r}, expected {expected!r}")


def summary():
    ok = tests_passed == tests_run
    print(f"\n{tests_passed}/{tests_run}  {'✅ ALL PASSED' if ok else '❌ SOME FAILED'}")
# -------------------------------------------------------------------------

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = len(t)                      # letters of t still missing from the window
        d = Counter(t)                     # d[c] > 0: still need c; <= 0: window has enough (or spare)
        l = 0
        best_len = float("inf")
        best_start = 0
        for r in range(len(s)):
            if d[s[r]] > 0:                # this letter still helps
                need -= 1
            d[s[r]] -= 1                   # subtract either way: extras go negative
            while need == 0:               # window is valid: try to shrink it
                if r - l + 1 < best_len:   # inclusive length; keep the SHORTEST
                    best_len = r - l + 1
                    best_start = l
                d[s[l]] += 1               # give the left letter back
                if d[s[l]] > 0:            # window is now short of it
                    need += 1
                l += 1

        return "" if best_len == float("inf") else s[best_start:best_start + best_len]


if __name__ == "__main__":
    sol = Solution()
    check(sol.minWindow("ADOBECODEBANC", "ABC"), "BANC")
    check(sol.minWindow("a", "a"), "a")
    check(sol.minWindow("a", "aa"), "")                      # not enough characters
    check(sol.minWindow("ab", "b"), "b")
    check(sol.minWindow("aa", "aa"), "aa")                   # duplicates in t
    check(sol.minWindow("ADOBECODEBANC", "AABC"), "ADOBECODEBA")
    check(sol.minWindow("bba", "ab"), "ba")
    summary()
