// 143. Reorder List
// https://leetcode.com/problems/reorder-list/
// Pattern : find middle + reverse second half + merge
// Time    : O(n)      Space: O(1)
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
    // L0 -> L1 -> ... -> Ln-1 -> Ln  becomes  L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 ...
    void reorderList(ListNode* head) {
        // TODO: 1) find middle (slow/fast)  2) reverse second half  3) merge the two halves alternately
        ListNode* f = head, * s = head;
        while(f != NULL && f->next != NULL){
            f = f->next->next;
            s = s->next;
        }
        ListNode* cur = s;
        ListNode* prev = NULL;
        while(cur != NULL){
            ListNode* temp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = temp;    
        }

        ListNode * first = head;
        ListNode* second = prev;

        while(second->next != NULL){
            ListNode* t1 = first->next;
            ListNode* t2 = second->next;
            first->next = second;
            second->next = t1;
            first = t1;
            second = t2;


        }

        

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
    ListNode* a = build({1, 2, 3, 4});     s.reorderList(a);
    check(toVec(a), vector<int>{1, 4, 2, 3});
    ListNode* b = build({1, 2, 3, 4, 5});  s.reorderList(b);
    check(toVec(b), vector<int>{1, 5, 2, 4, 3});
    ListNode* c = build({1});              s.reorderList(c);
    check(toVec(c), vector<int>{1});
    ListNode* d = build({1, 2});           s.reorderList(d);
    check(toVec(d), vector<int>{1, 2});
    summary();
    return 0;
}
