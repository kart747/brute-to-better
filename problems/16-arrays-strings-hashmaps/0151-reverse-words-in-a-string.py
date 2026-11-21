# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/
# Pattern : string methods (split, reverse, join)
# Time    : O(n)      Space: O(n)
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
    def reverseWords(self, s: str) -> str:
        # Reverse the ORDER of the words. Result has single spaces and no leading/trailing spaces.
        # "  hello   world  " -> "world hello".
        # Hint: .split() with NO argument splits on any amount of whitespace and drops empties.
        # Then reverse the list ([::-1] or reversed()) and " ".join(...) it.
        # split() drops extra spaces, reversed() flips the word order, join() glues with one space
        return " ".join(reversed(s.split()))



if __name__ == "__main__":
    s = Solution()
    check(s.reverseWords("the sky is blue"), "blue is sky the")
    check(s.reverseWords("  hello world  "), "world hello")
    check(s.reverseWords("a good   example"), "example good a")
    check(s.reverseWords("one"), "one")
    summary()
