// 53. Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/
// Pattern : Kadane's algorithm (running sum with reset)
// Time    : O(n)      Space: O(1)
// Solved  : 2026-09-24
//
// Idea: the best subarray ending at i either extends the one ending at i-1
// or starts fresh at i. A negative running sum can only hurt, so reset it to 0.
// Update max_sum BEFORE the reset, otherwise all-negative arrays return 0.

#include <bits/stdc++.h>
using namespace std;

// Brute force: every (start, end) pair with a running sum.  O(n^2) time, O(1) space.
int maxSubArrayBrute(vector<int>& nums) {
    int max_sum = INT_MIN;
    for (int i = 0; i < nums.size(); i++) {
        int sum = 0;
        for (int j = i; j < nums.size(); j++) {
            sum += nums[j];
            max_sum = max(max_sum, sum);
        }
    }
    return max_sum;
}

// Optimized: Kadane.  O(n) time, O(1) space.
int maxSubArray(vector<int>& nums) {
    int sum = 0, max_sum = INT_MIN;
    for (int i = 0; i < nums.size(); i++) {
        sum += nums[i];
        max_sum = max(max_sum, sum);
        if (sum < 0) sum = 0;
    }
    return max_sum;
}

int main() {
    vector<int> a = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << maxSubArray(a) << " " << maxSubArrayBrute(a) << "\n";  // 6 6

    vector<int> b = {5, 4, -1, 7, 8};
    cout << maxSubArray(b) << " " << maxSubArrayBrute(b) << "\n";  // 23 23

    vector<int> c = {-1, -2, -3};
    cout << maxSubArray(c) << " " << maxSubArrayBrute(c) << "\n";  // -1 -1
}
