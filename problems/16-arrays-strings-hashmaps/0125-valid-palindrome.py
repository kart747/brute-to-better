# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Pattern : two pointers (skip non-alphanumeric, compare lowercase)
# Time    : O(n)      Space: O(n)   (cleaned copy; two pointers would be O(1) space)
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
    def isPalindrome(self, s: str) -> bool:
        # Ignore case and ignore anything that is not a letter or digit.
        # "A man, a plan, a canal: Panama" -> True.
        # Easy way: build a cleaned string (use .lower() and .isalnum()), compare it to its reverse s[::-1].
        # Harder way (O(1) space): two pointers moving inward, skipping junk characters.
        # keep only letters/digits, lowercase them, then compare with the reverse
        cs ="".join(ch for ch in s if ch.isalnum()).lower()
        return cs == cs[::-1]


if __name__ == "__main__":
    s = Solution()
    check(s.isPalindrome("A man, a plan, a canal: Panama"), True)
    check(s.isPalindrome("race a car"), False)
    check(s.isPalindrome(" "), True)                # nothing left after cleaning -> palindrome
    check(s.isPalindrome("0P"), False)              # digits count, '0' != 'p'
    check(s.isPalindrome("ab_a"), True)             # underscore is NOT alphanumeric
    summary()
