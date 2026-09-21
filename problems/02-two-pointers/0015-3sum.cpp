// 15. 3Sum
// https://leetcode.com/problems/3sum/
// Pattern : sort + two pointers
// Time    : O(n^2)    Space: O(1) extra
// Status  : WIP (started 2026-09-12) - duplicate skipping for `right` still buggy
// TODO    : line comparing nums[right] with itself should compare with nums[right+1]

#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> threeSum(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    int n = nums.size();

    for (int i = 0; i < n; i++) {
        // TODO: skip duplicate values of nums[i]

        if(i!= 0 &&  nums[i-1] == nums[i]){
            continue;
        }
    
        // TODO: optional early-exit if nums[i] > 0



        int left = i + 1, right = n - 1;
        while (left < right) {
            int total = nums[i] + nums[left] + nums[right];

            if (total == 0) {
                // TODO: push {nums[i], nums[left], nums[right]} into result
                // TODO: move left++, right--
                // TODO: skip duplicates for both left and right
                result.push_back({nums[i],nums[left],nums[right]});
                left++;
                right--;
                while(left<right && nums[left] == nums[left-1]) left++;
                while(left<right && nums[right] == nums[right]) right--;

            } else if (total < 0) {
                left++;
            } else {
                right--;
            }
        }
    }

    return result;
}

int main() {
    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    vector<vector<int>> triplets = threeSum(nums);

    for (auto& t : triplets) {
        cout << "[" << t[0] << ", " << t[1] << ", " << t[2] << "]\n";
    }

    return 0;
}
