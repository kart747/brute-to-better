# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Pattern : hash map / Counter (compare the letter counts of both strings)
# Time    : O(n log n)  Space: O(n)   (sorting both strings; Counter version is O(n))
# Solved  : 2026-11-21

from collections import Counter

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
    def isAnagram(self, s: str, t: str) -> bool:
        # True if t is s with the letters rearranged (same letters, same counts).
        # Anagrams have the same letters, so sorting both gives the identical list.
        # (Different lengths -> different sorted lists -> False, so no separate length check needed.)
        return sorted(s) == sorted(t)
        # Counter version: return Counter(s) == Counter(t)


if __name__ == "__main__":
    s = Solution()
    check(s.isAnagram("anagram", "nagaram"), True)
    check(s.isAnagram("rat", "car"), False)
    check(s.isAnagram("a", "a"), True)
    check(s.isAnagram("ab", "a"), False)            # different lengths
    check(s.isAnagram("aacc", "ccac"), False)       # same letters, different counts
    summary()
