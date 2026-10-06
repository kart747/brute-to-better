// 19. Remove Nth Node From End of List
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// Pattern : fast & slow pointers (n-step gap) + dummy head
// Time    : O(L)      Space: O(1)
// Solved  : 2026-10-06

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode dummy(0, head);
    ListNode *f = &dummy, *s = &dummy;

    for (int i = 0; i <= n; i++) {   // 1) make the gap once (n+1 steps)
        f = f->next;
    }
    while (f != NULL) {              // 2) walk both together
        f = f->next;
        s = s->next;
    }
    s->next = s->next->next;         // 3) s is just before the target, so unlink
    return dummy.next;
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
    check(toVec(s.removeNthFromEnd(build({1, 2, 3, 4, 5}), 2)), vector<int>{1, 2, 3, 5});
    check(toVec(s.removeNthFromEnd(build({1}), 1)),             vector<int>{});         // list becomes empty
    check(toVec(s.removeNthFromEnd(build({1, 2}), 1)),          vector<int>{1});        // remove tail
    check(toVec(s.removeNthFromEnd(build({1, 2}), 2)),          vector<int>{2});        // remove head
    summary();
    return 0;
}
