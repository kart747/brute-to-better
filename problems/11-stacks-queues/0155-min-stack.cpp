// 155. Min Stack
// https://leetcode.com/problems/min-stack/
// Pattern : stack (track running minimum alongside each value)
// Time    : O(1) per op      Space: O(n)
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

class MinStack {
public:
    stack<pair<int,int>> st; 
    MinStack() {
        // TODO
        

    }

    void push(int val) {
        // TODO
        int mn;
        if(st.empty()) mn = val;
        else mn = min(st.top().second,val);   // .second = min so far (not the previous value)
        st.push({val,mn});

    }

    void pop() {
        st.pop();
    }

    int top() {
        // TODO
        if(!st.empty()) return st.top().first;
        return -1;
    }

    int getMin() {
        // TODO
        if(!st.empty()) return st.top().second;
        return -1;
    }
};

int main() {
    MinStack m;
    m.push(-2);
    m.push(0);
    m.push(-3);
    check(m.getMin(), -3);
    m.pop();
    check(m.top(), 0);
    check(m.getMin(), -2);
    m.push(-2);
    m.pop();
    check(m.getMin(), -2);
    summary();
    return 0;
}
