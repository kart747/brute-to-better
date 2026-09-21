// 2461. Maximum Sum of Distinct Subarrays With Length K
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
// Pattern : fixed-size sliding window + frequency map
// Time    : O(n)      Space: O(k)
// Solved  : 2026-09-22

#include <bits/stdc++.h>
using namespace std;

long long maximumSubarraySum(vector<int>& nums, int k) {
    int n = nums.size();

    if (k > n) return 0;

    unordered_map<int, int> freq;
    long long sum = 0;
    long long best = 0;

    // Build first window
    for (int i = 0; i < k; i++) {
        sum += nums[i];
        freq[nums[i]]++;
    }

    // Check first window
    if (freq.size() == k) {
        best = max(best, sum);
    }

    int left = 0;

    // Slide the window
    for (int right = k; right < n; right++) {

        // Add right element
        sum += nums[right];
        freq[nums[right]]++;

        // Remove left element
        sum -= nums[left];
        freq[nums[left]]--;

        if (freq[nums[left]] == 0) {
            freq.erase(nums[left]);
        }

        left++;

        // Check current window
        if (freq.size() == k) {
            best = max(best, sum);
        }
    }

    return best;
}

int main() {
    vector<int> a = {1, 5, 4, 2, 9, 9, 9};
    cout << maximumSubarraySum(a, 3) << "\n";  // 15

    vector<int> b = {4, 4, 4};
    cout << maximumSubarraySum(b, 3) << "\n";  // 0
}