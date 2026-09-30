// 724. Find Pivot Index
// https://leetcode.com/problems/find-pivot-index/
// Pattern : prefix sum
// Time    : O(n)      Space: O(1)
// Solved  : 2026-09-30

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        int s = 0, p = 0;
        for(int i =0;i<n;i++){
            s+=nums[i];
        }
        for(int i =0;i<n;i++){
            if(p == s-p - nums[i]){
                return i;
            }
            p+=nums[i];
        }
        return -1;


    }
};

int main() {
    Solution sol;

    vector<int> nums1 = {1, 7, 3, 6, 5, 6};
    cout << sol.pivotIndex(nums1) << "\n"; // expected 3

    vector<int> nums2 = {1, 2, 3};
    cout << sol.pivotIndex(nums2) << "\n"; // expected -1

    vector<int> nums3 = {2, 1, -1};
    cout << sol.pivotIndex(nums3) << "\n"; // expected 0

    return 0;
}
