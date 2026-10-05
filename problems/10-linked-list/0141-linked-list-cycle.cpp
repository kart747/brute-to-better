// 141. Linked List Cycle
// https://leetcode.com/problems/linked-list-cycle/
// Pattern : fast & slow pointers (Floyd's cycle detection)
// Time    : O(n)      Space: O(1)
// Solved  : 2026-10-05

#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode* head) {
        ListNode *slow = head, *fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) return true;
        }
        return false;
    }
};

// helper for local testing: tail links back to node at index pos (-1 = no cycle)
ListNode* build(const vector<int>& v, int pos) {
    ListNode* head = NULL;
    ListNode* tail = NULL;
    ListNode* target = NULL;
    for (int i = 0; i < (int)v.size(); i++) {
        ListNode* node = new ListNode(v[i]);
        if (!head) head = node;
        else tail->next = node;
        tail = node;
        if (i == pos) target = node;
    }
    if (tail) tail->next = target;
    return head;
}

int main() {
    Solution s;
    cout << boolalpha;
    cout << s.hasCycle(build({3, 2, 0, -4}, 1)) << "\n";   // expected true
    cout << s.hasCycle(build({1, 2}, 0)) << "\n";          // expected true
    cout << s.hasCycle(build({1}, -1)) << "\n";            // expected false
    cout << s.hasCycle(build({}, -1)) << "\n";             // expected false
    cout << s.hasCycle(build({1, 2, 3, 4}, -1)) << "\n";   // expected false
    cout << s.hasCycle(build({1}, 0)) << "\n";            // expected true (self-loop)
    return 0;
}
