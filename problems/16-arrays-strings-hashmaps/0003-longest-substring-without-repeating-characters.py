# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Pattern : sliding window + set (or dict of last-seen index)
# Time    : O(n)      Space: O(min(n, alphabet))  (each char enters and leaves the window once)
# Solved  : 2026-11-20


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
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Length of the longest substring with all distinct characters.
        # Window [left, right]: grow right; if s[right] is already in the window, shrink from left.
        seen = set()                 # letters currently inside the window [left, right]
        left = 0
        best = 0
        for right in range(len(s)):
            while s[right] in seen:      # duplicate: shrink from the left until it's gone
                seen.remove(s[left])
                left+=1
            seen.add(s[right])           # add AFTER clearing the duplicate
            best = max(best, right - left + 1)

        return best


if __name__ == "__main__":
    s = Solution()
    check(s.lengthOfLongestSubstring("abcabcbb"), 3)
    check(s.lengthOfLongestSubstring("bbbbb"), 1)
    check(s.lengthOfLongestSubstring("pwwkew"), 3)
    check(s.lengthOfLongestSubstring(""), 0)
    check(s.lengthOfLongestSubstring("abba"), 2)          # classic left-pointer-moves-backwards trap
    summary()
