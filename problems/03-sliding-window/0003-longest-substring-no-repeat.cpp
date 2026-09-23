// 3. Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Pattern : variable-size sliding window + frequency map
// Time    : O(n)      Space: O(min(n, charset))
// Solved  : 2026-09-23
//
// Invariant: the window [j, i] always holds distinct characters. After adding
// s[i], the only character that can possibly repeat is s[i] itself, so we
// shrink from the left until its count drops back to 1. The answer is the
// largest window width seen while the invariant holds.
//
// The inner while loop runs at most n times in total across the whole
// function (each index is added once by i and removed at most once by j),
// so this is amortized O(1) per step, not a nested O(n^2) loop.

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        unordered_map<char, int> freq;
        int j = 0;    // left edge of the window
        int ans = 0;

        for (int i = 0; i < n; i++) {
            // Grow the window to the right.
            freq[s[i]]++;

            // s[i] is the only possible duplicate; shrink until it is unique again.
            while (freq[s[i]] > 1) {
                --freq[s[j++]];
            }

            // Window [j, i] is now duplicate-free.
            ans = max(ans, i - j + 1);
        }
        return ans;
    }
};

int main() {
    Solution sol;

    cout << sol.lengthOfLongestSubstring("abcabcbb") << "\n";  // 3  ("abc")
    cout << sol.lengthOfLongestSubstring("bbbbb") << "\n";     // 1  ("b")
    cout << sol.lengthOfLongestSubstring("pwwkew") << "\n";    // 3  ("wke")
    cout << sol.lengthOfLongestSubstring("") << "\n";          // 0  empty string
    cout << sol.lengthOfLongestSubstring("a") << "\n";         // 1  single char
    cout << sol.lengthOfLongestSubstring("abcdef") << "\n";    // 6  all distinct
    cout << sol.lengthOfLongestSubstring("dvdf") << "\n";      // 3  ("vdf") — left
                                                               // pointer must jump
                                                               // past the first 'd'
    cout << sol.lengthOfLongestSubstring("tmmzuxt") << "\n";   // 5  ("mzuxt")

    return 0;
}
