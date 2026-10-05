// 876. Middle of the Linked List
// https://leetcode.com/problems/middle-of-the-linked-list/
// Pattern : <fill in after solving>
// Time    : O(?)      Space: O(?)
// Solved  : <YYYY-MM-DD>

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

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        // TODO: brute force first, then optimize
        return head;
    }
};

// helpers for local testing
ListNode* build(const vector<int>& v) {
    ListNode dummy;
    ListNode* tail = &dummy;
    for (int x : v) {
        tail->next = new ListNode(x);
        tail = tail->next;
    }
    return dummy.next;
}

vector<int> toVec(ListNode* head) {
    vector<int> v;
    for (ListNode* cur = head; cur; cur = cur->next) v.push_back(cur->val);
    return v;
}

int main() {
    Solution s;
    check(toVec(s.middleNode(build({1, 2, 3, 4, 5}))),    vector<int>{3, 4, 5});
    check(toVec(s.middleNode(build({1, 2, 3, 4, 5, 6}))), vector<int>{4, 5, 6});  // even length -> second middle
    check(toVec(s.middleNode(build({1}))),                vector<int>{1});
    check(toVec(s.middleNode(build({1, 2}))),             vector<int>{2});
    summary();
    return 0;
}
