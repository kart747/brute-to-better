# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# Pattern : hash map count + sort by frequency (or heap / bucket sort)
# Time    : O(n log k)  Space: O(n)   (Counter is O(n); most_common(k) uses a heap of size k)
# Solved  : 2026-11-20

from collections import Counter
import heapq

# ---- test helper: one PASS/FAIL line per case + a summary at the end ----
tests_run = tests_passed = 0

from collections import Counter
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
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Return the k most frequent elements (any order).
        # Start simple: Counter + sorted by count. Later: Counter.most_common, heapq.nlargest, bucket sort.
        count = Counter(nums)               # number -> how many times it appears
        ans = count.most_common(k)          # top k as (number, count) pairs, highest count first

        return [val for val, cnt in ans]    # keep only the numbers, drop the counts




if __name__ == "__main__":
    s = Solution()
    check(sorted(s.topKFrequent([1, 1, 1, 2, 2, 3], 2)), [1, 2])
    check(sorted(s.topKFrequent([1], 1)), [1])
    check(sorted(s.topKFrequent([4, 4, 4, 5, 5, 6, 6, 6, 6], 1)), [6])
    check(sorted(s.topKFrequent([-1, -1, 2, 2, 3], 2)), [-1, 2])
    summary()
