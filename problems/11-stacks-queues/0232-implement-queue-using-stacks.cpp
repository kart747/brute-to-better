// 232. Implement Queue using Stacks
// https://leetcode.com/problems/implement-queue-using-stacks/
// Pattern : two stacks (lazy transfer from in to out)
// Time    : O(1) amortized      Space: O(n)
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

class MyQueue {
public:
    stack<int> st1;
    stack<int> st2;
    MyQueue() {
        // TODO

    }

    void push(int x) {
        // TODO
        st1.push(x);
    }

    int pop() {
        // TODO
        if(!st2.empty()){
            int t = st2.top();
            st2.pop();
            return t;

        }  
        if(st1.empty()) return -1;
        if(st2.empty() && !st1.empty()){
            while(!st1.empty()){
                int temp = st1.top();
                st2.push(temp);
                st1.pop();
            }
            int t = st2.top();
            st2.pop();
            return t;
        }
        return -1;
    }

    int peek() {
        if(!st2.empty()) return st2.top();
        if(st1.empty()) return -1;
        if(st2.empty() && !st1.empty()){
            while(!st1.empty()){
                int temp = st1.top();
                st1.pop();
                st2.push(temp);
            }
            return st2.top();
        }
        return -1;
    }

    bool empty() {
        if(st2.empty() && st1.empty()) return true;
        return false;
    }
};

int main() {
    MyQueue q;
    q.push(1);
    q.push(2);
    check(q.peek(), 1);
    check(q.pop(), 1);
    check(q.empty(), false);
    q.push(3);
    check(q.pop(), 2);
    check(q.pop(), 3);
    check(q.empty(), true);
    summary();
    return 0;
}
