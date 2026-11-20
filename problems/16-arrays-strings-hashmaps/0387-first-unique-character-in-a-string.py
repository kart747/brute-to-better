# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/
# Pattern : hash map (count characters, then scan the string in order)
# Time    : O(n)      Space: O(1) (at most 26 lowercase letters in the Counter)
# Solved  : 2026-11-20

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
    def firstUniqChar(self, s: str) -> int:
        # Return the INDEX of the first character that appears exactly once, else -1.
        # Plan: pass 1 = count every char. Pass 2 = walk the string (with its index) in order.
        count = Counter(s)

        for i, ch in enumerate(s):   # walk the STRING so i is a string index
            if count[ch] == 1:
                return i
        return -1

if __name__ == "__main__":
    s = Solution()
    check(s.firstUniqChar("leetcode"), 0)
    check(s.firstUniqChar("loveleetcode"), 2)
    check(s.firstUniqChar("aabb"), -1)
    check(s.firstUniqChar("z"), 0)
    check(s.firstUniqChar("aadadaad"), -1)
    summary()
