# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# Pattern : string scan (shrink a prefix until every word starts with it)
# Time    : O(S)      Space: O(1)   (S = total number of characters across all words)
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
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Longest string that every word in strs starts with ("" if none).
        # Idea: take the first word as the prefix; while some word does not .startswith(prefix),
        # chop the last letter off the prefix.
        prefix = strs[0]                      # start with the whole first word

        for word in strs:
            while not word.startswith(prefix):  # this word doesn't start with the prefix?
                prefix = prefix[:-1]          # chop the last letter off
        return prefix


if __name__ == "__main__":
    s = Solution()
    check(s.longestCommonPrefix(["flower", "flow", "flight"]), "fl")
    check(s.longestCommonPrefix(["dog", "racecar", "car"]), "")
    check(s.longestCommonPrefix(["a"]), "a")
    check(s.longestCommonPrefix(["abc", "abc", "abc"]), "abc")
    check(s.longestCommonPrefix(["", "b"]), "")
    summary()
