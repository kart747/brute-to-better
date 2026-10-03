// 875. Koko Eating Bananas
// https://leetcode.com/problems/koko-eating-bananas/
// Pattern : binary search on answer
// Time    : O(n log m) Space: O(1)   (m = max pile)
// Solved  : 2026-10-03

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long canFinish(vector<int>& piles,int k){
        int n = piles.size();
        long long hours = 0;
        for(int i = 0;i<n;i++){
            hours += (piles[i] + k - 1) / k;

        }
        return hours;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int lo = 1;
        int hi = *max_element(piles.begin(), piles.end());
        while(lo<hi){
            int mid = (lo+hi)/2;
            long long temp = canFinish(piles,mid);
            if(h >= temp ){
                hi = mid;
                
            }
            else{
                lo = mid+1;
            }
        }

        return lo;
    }
};

int main() {
    Solution s;
    vector<int> a = {3, 6, 7, 11};
    cout << s.minEatingSpeed(a, 8) << "\n";   // expected 4
    vector<int> b = {30, 11, 23, 4, 20};
    cout << s.minEatingSpeed(b, 5) << "\n";   // expected 30
    cout << s.minEatingSpeed(b, 6) << "\n";   // expected 23
    return 0;
}
