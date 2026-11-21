# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/
# Pattern : two hash maps (s-char -> t-char and t-char -> s-char)
# Time    : O(n)      Space: O(1)   (at most one entry per distinct character)
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
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Can you replace letters in s to get t, with every letter mapping to exactly ONE letter
        # and no two letters mapping to the same one? "egg" -> "add" yes, "foo" -> "bar" no.
        # Hint: you need to check the mapping in BOTH directions. zip(s, t) walks both strings together.
        s_to_t = {}   # letter in s -> letter in t
        t_to_s = {}   # letter in t -> letter in s (catches two s-letters mapping to the same t-letter)

        for a,b in zip(s,t):
            if a in s_to_t and s_to_t[a] != b:
                return False
            if b in t_to_s and t_to_s[b] != a:
                return False
            s_to_t[a] = b
            t_to_s[b] = a
        return True


if __name__ == "__main__":
    s = Solution()
    check(s.isIsomorphic("egg", "add"), True)
    check(s.isIsomorphic("foo", "bar"), False)
    check(s.isIsomorphic("paper", "title"), True)
    check(s.isIsomorphic("badc", "baba"), False)    # two different letters map to the same 'a'
    check(s.isIsomorphic("ab", "aa"), False)
    summary()
