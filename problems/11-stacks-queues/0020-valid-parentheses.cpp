// 20. Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/
// Pattern : stack (match closing with last opening)
// Time    : O(n)      Space: O(n)
// Solved  : 2026-10-07

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
    bool isValid(string s) {
        stack <char> st;
        for (auto t : s){
            
           if (t == '(' || t == '{' || t == '[')
            {
                st.push(t);
            }
            else{
                if(st.empty()) return false;
                char temp = st.top();
                if(temp == '(' && t == ')' || temp == '{' && t == '}'|| temp == '[' && t == ']' ){
                    st.pop();
                }
                else return false;
            }
        }
        if(st.empty()) return true;
        return false;
    }
};

int main() {
    Solution s;
    check(s.isValid("()"), true);
    check(s.isValid("()[]{}"), true);
    check(s.isValid("(]"), false);
    check(s.isValid("([)]"), false);
    check(s.isValid("{[]}"), true);
    check(s.isValid("("), false);
    check(s.isValid("]"), false);
    summary();
    return 0;
}
