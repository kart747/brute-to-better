// 739. Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/
// Pattern : monotonic stack (indices of decreasing temps)
// Time    : O(n)      Space: O(n)
// Solved  : 2026-10-13

#include <bits/stdc++.h>
using namespace std;

// ---- test helpers: one PASS/FAIL line per case + a summary at the end ----
template <class T> string show(const T& x) { ostringstream o; o << boolalpha << x; return o.str(); }
template <class T> string show(const vector<T>& v) {
    string s = "[";
    for (size_t i = 0; i < v.size(); i++) s += (i ? "," : "") + show(v[i]);
    return s + "]";
}
int tests_run = 0, tests_passed = 0;
template <class T, class U> void check(const T& got, const U& expected) {
    tests_run++;
    if (got == expected) { tests_passed++; cout << "✅ PASS #" << tests_run << "\n"; }
    else cout << "❌ FAIL #" << tests_run << "  got " << show(got) << ", expected " << show(expected) << "\n";
}
void summary() {
    cout << "\n" << tests_passed << "/" << tests_run
         << (tests_passed == tests_run ? "  ✅ ALL PASSED" : "  ❌ SOME FAILED") << "\n";
}
// ---------------------------------------------------------------------------

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
    int n = temperatures.size();
    stack<int> st;                 // indices of days still waiting for a warmer day
    vector<int> ans(n, 0);

    for (int i = 0; i < n; i++) {
        while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
            int j = st.top();
            st.pop();
            ans[j] = i - j;        // days waited
        }
        st.push(i);
    }
    return ans;
}

};

int main() {
    Solution s;
    vector<int> a = {73,74,75,71,69,72,76,73};
    check(s.dailyTemperatures(a), vector<int>{1,1,4,2,1,1,0,0});
    vector<int> b = {30,40,50,60};
    check(s.dailyTemperatures(b), vector<int>{1,1,1,0});
    vector<int> c = {30,60,90};
    check(s.dailyTemperatures(c), vector<int>{1,1,0});
    vector<int> d = {90,80,70};
    check(s.dailyTemperatures(d), vector<int>{0,0,0});
    summary();
    return 0;
}
