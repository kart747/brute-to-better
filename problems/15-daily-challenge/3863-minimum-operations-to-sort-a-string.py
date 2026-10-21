# 3863. Minimum Operations to Sort a String   (LeetCode daily, 2026-10-21)
# https://leetcode.com/problems/minimum-operations-to-sort-a-string/
# Pattern : string / case analysis (answer is a small number)
# Time    : O(n)      Space: O(n) (the slices s[:-1] / s[1:]; O(1) with index loops)
# Solved  : 2026-10-21


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
    def minOperations(self, s: str) -> int:
        n = len(s)
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0                                   # already sorted
        if n == 2:
            return -1                                  # only length-1 substrings allowed: can't fix "ba"
        # one op can only sort a prefix or a suffix of length n-1 (or something in the middle)
        if s[0] == min(s) or s[-1] == max(s):
            return 1                                   # sort the suffix s[1:] / the prefix s[:-1]
        # two ops: sort prefix then suffix (needs min(s[:-1]) <= s[-1]),
        #          or sort suffix then prefix (needs max(s[1:]) >= s[0])
        if min(s[:-1]) <= s[-1] or max(s[1:]) >= s[0]:
            return 2
        return 3                                       # s[0] strictly biggest AND s[-1] strictly smallest


if __name__ == "__main__":
    sol = Solution()
    # expected values come from a brute-force BFS over all substring sorts (not the entire string)
    check(sol.minOperations("dog"), 1)
    check(sol.minOperations("card"), 2)
    check(sol.minOperations("gf"), -1)
    check(sol.minOperations("a"), 0)
    check(sol.minOperations("ab"), 0)
    check(sol.minOperations("cba"), 3)
    check(sol.minOperations("bca"), 2)
    check(sol.minOperations("bac"), 1)
    check(sol.minOperations("acb"), 1)
    check(sol.minOperations("aaa"), 0)
    check(sol.minOperations("baa"), 2)
    check(sol.minOperations("zyxwv"), 3)
    summary()
