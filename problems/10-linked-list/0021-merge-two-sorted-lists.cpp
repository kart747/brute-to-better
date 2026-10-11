// 21. Merge Two Sorted Lists
// https://leetcode.com/problems/merge-two-sorted-lists/
// Pattern : dummy head + tail pointer (relink existing nodes)
// Time    : O(m + n)  Space: O(1)
// Solved  : 2026-10-11

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
    // Merge two ascending lists into one ascending list by relinking nodes.
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy;              // fake node before the real head
        ListNode* tail = &dummy;     // last node of the merged list so far

        while (list1 != NULL && list2 != NULL) {
            if (list1->val <= list2->val) {
                tail->next = list1;
                list1 = list1->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
            }
            tail = tail->next;
        }

        // one list is exhausted; the other is already sorted, attach it whole
        tail->next = (list1 != NULL) ? list1 : list2;
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
    check(toVec(s.mergeTwoLists(build({1, 2, 4}), build({1, 3, 4}))), vector<int>{1, 1, 2, 3, 4, 4});
    check(toVec(s.mergeTwoLists(build({}), build({}))),               vector<int>{});
    check(toVec(s.mergeTwoLists(build({}), build({0}))),              vector<int>{0});
    check(toVec(s.mergeTwoLists(build({5}), build({}))),              vector<int>{5});
    check(toVec(s.mergeTwoLists(build({1, 3, 5}), build({2, 4}))),    vector<int>{1, 2, 3, 4, 5});
    check(toVec(s.mergeTwoLists(build({1, 2}), build({3, 4, 5}))),    vector<int>{1, 2, 3, 4, 5});
    summary();
    return 0;
}
