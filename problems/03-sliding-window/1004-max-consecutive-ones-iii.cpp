// 1004. Max Consecutive Ones III
// https://leetcode.com/problems/max-consecutive-ones-iii/
// Pattern : variable-size sliding window (count zeros in window)
// Time    : O(n)      Space: O(1)
// Solved  : 2026-10-04

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int n = nums.size();
        int z = 0;
        int i = 0,j = 0;
        int count = 0,mcount = 0;

        while(j<n){
            if(nums[j] == 0){
                z++;

            }

            
            while(z>k){
                if(nums[i] == 0){
                    z--;
                }
                i++;
            }
            count = j - i + 1;
            mcount = max(count,mcount);
            j++;


        }
        return mcount;
    }
};

int main() {
    Solution s;
    vector<int> a = {1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0};
    cout << s.longestOnes(a, 2) << "\n";   // expected 6
    vector<int> b = {0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1};
    cout << s.longestOnes(b, 3) << "\n";   // expected 10
    return 0;
}
