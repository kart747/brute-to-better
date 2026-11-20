# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Pattern : hash map (key = something identical for all anagrams, value = list of words)
# Time    : O(n * k log k)   Space: O(n * k)   (n words, k = longest word, sorting each word)
# Solved  : 2026-11-20

from collections import defaultdict

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

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Group words that are anagrams of each other. Any group order is fine.
        # Think: what can you compute from a word so that all its anagrams get the SAME key?
        # (a list can't be a dict key, but a tuple / string can)
        # Idea: anagrams have the SAME letters, so if you sort the letters of each word,
        # all anagrams turn into the identical string ("eat","tea","ate" -> "aet").
        # Use that sorted string as a dict key; the value is the list of words that share it.

        # defaultdict(list): a key we haven't seen yet automatically starts as []
        # (note: `list` the type, NOT `strs` and NOT `list()`).
        group = defaultdict(list)

        for word in strs:
            # sorted(word) gives a LIST of letters, and a list can't be a dict key.
            # "".join(...) glues them into a string, which can be a key.
            key = "".join(sorted(word))

            # add this word to the group for its key (no KeyError thanks to defaultdict)
            group[key].append(word)

        # .values() is a dict_values object, so wrap it in list() to return a real list of lists.
        return list(group.values())


if __name__ == "__main__":
    s = Solution()
    def norm(groups):                      # group order / word order inside a group don't matter
        return sorted(sorted(g) for g in groups)

    check(norm(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])),
          [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])
    check(norm(s.groupAnagrams([""])), [[""]])
    check(norm(s.groupAnagrams(["a"])), [["a"]])
    check(norm(s.groupAnagrams(["ab", "ba", "abc"])), [["ab", "ba"], ["abc"]])
    summary()
