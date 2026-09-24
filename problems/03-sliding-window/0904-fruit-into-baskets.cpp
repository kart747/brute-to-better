// 904. Fruit Into Baskets
// https://leetcode.com/problems/fruit-into-baskets/
// Pattern : variable-size sliding window + frequency map
// Time    : O(n)      Space: O(1)
// Solved  : 2026-09-24

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        unordered_map<int,int> mp;
        int j = 0, n = fruits.size(), ans = 0;
        for (int i = 0; i < n; i++) {
            mp[fruits[i]]++;
            while (mp.size() > 2) {
                --mp[fruits[j]];
                if (mp[fruits[j]] == 0) {
                    mp.erase(fruits[j]);
                }
                j++;
            }
            ans = max(ans, i - j + 1);
        }
        return ans;
    }
};

int main() {
    Solution s;
    vector<int> a = {1, 2, 1};
    cout << s.totalFruit(a) << "\n";  // 3

    vector<int> b = {0, 1, 2, 2};
    cout << s.totalFruit(b) << "\n";  // 3

    vector<int> c = {1, 2, 3, 2, 2};
    cout << s.totalFruit(c) << "\n";  // 4
}
