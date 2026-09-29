// 560. Subarray Sum Equals K
// https://leetcode.com/problems/subarray-sum-equals-k/
// Pattern : prefix sum
// Time    : O(n)       Space: O(n)
// Solved  : 2026-09-30

#include <bits/stdc++.h>
using namespace std;

// prefix sum + hashmap: need = sum - k, count occurrences of need seen so far
int subarraySum(vector<int>& nums, int k) {
    int count = 0;
    unordered_map <int,int> mp;
    mp[0]++;
    int sum = 0;
    for(int i = 0;i<nums.size();i++){
        sum+= nums[i];
        int need = sum - k;
        if(mp.find(need) != mp.end()){
            count = count + mp[need];
        }
        mp[sum]++;
            
        
    }
    return count;
    
    return 0;
}

int main() {
    vector<int> nums1 = {1, 1, 1};
    cout << subarraySum(nums1, 2) << "\n"; // expected 2

    vector<int> nums2 = {1, 2, 3};
    cout << subarraySum(nums2, 3) << "\n"; // expected 2

    vector<int> nums3 = {1, -1, 0};
    cout << subarraySum(nums3, 0) << "\n"; // expected 3

    vector<int> nums4 = {-1, -1, 1};
    cout << subarraySum(nums4, 0) << "\n"; // expected 1

    vector<int> nums5 = {0, 0, 0};
    cout << subarraySum(nums5, 0) << "\n"; // expected 6

    vector<int> nums6 = {5};
    cout << subarraySum(nums6, 5) << "\n"; // expected 1

    vector<int> nums7 = {5};
    cout << subarraySum(nums7, 0) << "\n"; // expected 0

    vector<int> nums8 = {1, 2, 3};
    cout << subarraySum(nums8, 100) << "\n"; // expected 0

    vector<int> nums9 = {3, 4, 7, 2, -3, 1, 4, 2};
    cout << subarraySum(nums9, 7) << "\n"; // expected 4

    vector<int> nums10 = {1, 2, -3};
    cout << subarraySum(nums10, -3) << "\n"; // expected 1

    vector<int> nums11 = {-1, -1, -1};
    cout << subarraySum(nums11, -2) << "\n"; // expected 2

    vector<int> nums12 = {1, 1, 1, 1};
    cout << subarraySum(nums12, 2) << "\n"; // expected 3

    return 0;
}
