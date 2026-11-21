# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# Pattern : expand around the center (odd and even centers)
# Time    : O(n^2)    Space: O(1) extra (the slices are at most O(n))
# Solved  : 2026-11-21


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
    def longestPalindrome(self, s: str) -> str:
        # Return the longest substring that reads the same forwards and backwards.
        # Idea: every palindrome has a center. For each index i, expand outward while the
        # two ends match: once with center (i, i) for odd length, once with (i, i+1) for even.
        # Keep the best (start, length) seen. Slice s[start:start+length] at the end.
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]        # the last valid window, not including l and r
        best = ""
        for i in range(len(s)):
            odd  = expand(i, i)
            even = expand(i, i + 1)       # even-length center sits between i and i+1
            best = max(best, odd, even, key=len)   # pick the longest of the three
        return best


if __name__ == "__main__":
    s = Solution()
    check(s.longestPalindrome("babad") in ("bab", "aba"), True)    # either is valid
    check(s.longestPalindrome("cbbd"), "bb")
    check(s.longestPalindrome("a"), "a")
    check(s.longestPalindrome("abcd") in ("a", "b", "c", "d"), True)
    check(s.longestPalindrome("racecar"), "racecar")
    summary()
