// 206. Reverse Linked List
// https://leetcode.com/problems/reverse-linked-list/
// Pattern : linked list pointer reversal (iterative)
// Time    : O(n)      Space: O(1)
// Solved  : 2026-10-04

#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* cur = head;
        ListNode* prev = NULL;

        while(cur != NULL){
            
            ListNode* temp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = temp;
            

        }
        return prev;
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

void print(ListNode* head) {
    cout << "[";
    for (ListNode* cur = head; cur; cur = cur->next) {
        cout << cur->val << (cur->next ? "," : "");
    }
    cout << "]\n";
}

int main() {
    Solution s;
    print(s.reverseList(build({1, 2, 3, 4, 5})));   // expected [5,4,3,2,1]
    print(s.reverseList(build({1, 2})));            // expected [2,1]
    print(s.reverseList(build({})));                // expected []  (LeetCode runtime error case)
    print(s.reverseList(build({7})));               // expected [7]
    return 0;
}
