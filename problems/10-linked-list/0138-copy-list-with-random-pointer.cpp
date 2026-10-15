// 138. Copy List with Random Pointer
// https://leetcode.com/problems/copy-list-with-random-pointer/
// Pattern : hash map old->new  OR  interleave copies (O(1) space)
// Time    : O(n)      Space: O(n)  (hash map version)
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

class Node {
public:
    int val;
    Node* next;
    Node* random;
    Node(int _val) : val(_val), next(nullptr), random(nullptr) {}
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        // TODO: deep copy -- every new node must be a NEW node, none shared with the original
        Node* cur = head;
        unordered_map<Node*, Node*> mp;         // old node -> its copy

        for (Node* cur = head; cur != NULL; cur = cur->next) {
            mp[cur] = new Node(cur->val);       // pass 1: one new node per original
        }
        mp[nullptr] = nullptr;

        for (Node* cur = head; cur != NULL; cur = cur->next) {
            mp[cur]->next   = mp[cur->next];        // copy's next = copy of original's next
            mp[cur]->random = mp[cur->random];      // copy's random = copy of original's random

        }


        return mp[head];

    }
};

// helpers for local testing
// spec: {value, index of random node or -1}, e.g. {{7,-1},{13,0}} = [7,null],[13,0]
Node* build(const vector<vector<int>>& spec) {
    vector<Node*> nodes;
    for (auto& p : spec) nodes.push_back(new Node(p[0]));
    for (size_t i = 0; i < nodes.size(); i++) {
        if (i + 1 < nodes.size()) nodes[i]->next = nodes[i + 1];
        if (spec[i][1] >= 0) nodes[i]->random = nodes[spec[i][1]];
    }
    return nodes.empty() ? nullptr : nodes[0];
}

// back to the same spec form so check() can compare it
vector<vector<int>> toSpec(Node* head) {
    map<Node*, int> idx;
    int i = 0;
    for (Node* c = head; c; c = c->next) idx[c] = i++;
    vector<vector<int>> v;
    for (Node* c = head; c; c = c->next) v.push_back({c->val, c->random ? idx[c->random] : -1});
    return v;
}

// true if the copy shares NO node with the original (a real deep copy)
bool noSharedNodes(Node* a, Node* b) {
    set<Node*> orig;
    for (Node* c = a; c; c = c->next) orig.insert(c);
    for (Node* c = b; c; c = c->next) {
        if (orig.count(c)) return false;
        if (c->random && orig.count(c->random)) return false;
    }
    return true;
}

int main() {
    Solution s;
    vector<vector<vector<int>>> cases = {
        {{7,-1},{13,0},{11,4},{10,2},{1,0}},   // LeetCode example 1
        {{1,1},{2,1}},                          // example 2
        {{3,-1},{3,0},{3,-1}},                  // example 3 (duplicate values)
        {{5,0}},                                // random points to itself
    };
    for (auto& spec : cases) {
        Node* orig = build(spec);
        Node* copy = s.copyRandomList(orig);
        check(toSpec(copy), spec);              // same structure
        check(noSharedNodes(orig, copy), true); // but all new nodes
    }
    check(s.copyRandomList(nullptr) == nullptr, true);  // empty list
    summary();
    return 0;
}
