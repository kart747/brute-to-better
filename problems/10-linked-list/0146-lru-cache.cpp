// 146. LRU Cache
// https://leetcode.com/problems/lru-cache/
// Pattern : hash map + doubly linked list (sentinel head/tail)
// Time    : O(1) get/put   Space: O(capacity)
// Solved  : 2026-10-14

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

class LRUCache {
public:
    struct Node {
        int val,key;
        Node* next,*prev;
        Node(int k, int v) : key(k), val(v), prev(nullptr), next(nullptr) {}
    };
    
    unordered_map<int,Node*> mp;
    int cap;
    Node* head,*tail;
    LRUCache(int capacity) {
        cap = capacity;
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head->next = tail;
        tail->prev = head;

    }
    void delNode(Node* n){
        n->next->prev = n->prev;
        n->prev->next = n->next;
    }
    void insertAfterhead(Node* n){
        head->next->prev = n;
        n->next = head->next;
        head->next = n;
        n->prev = head;
        
    }

    int get(int key) {
        // TODO: if key missing return -1; else move its node to the front (most recent) and return value
        if(mp.find(key) == mp.end()) return -1;
        Node* n = mp[key];
        delNode(n);
        insertAfterhead(n);
        return n->val;
    }

    void put(int key, int value) {
        // TODO: if key exists update value + move to front; else insert at front,
        //       and if size > capacity remove the node just before the tail (least recent) + erase from map
        if(mp.find(key) != mp.end()){
            Node* n = mp[key];
            n->val = value;
            delNode(n);
            insertAfterhead(n);
        } else {
            Node* n = new Node(key, value);
            mp[key] = n;
            insertAfterhead(n);
            if((int)mp.size() > cap){
                Node* lru = tail->prev;   // least recently used = just before tail
                delNode(lru);
                mp.erase(lru->key);       // node stores its key so we can erase it from the map
                delete lru;               // evicted for good, safe to free
            }
        }
    }
};

int main() {
    // LeetCode example 1, capacity 2
    LRUCache c(2);
    c.put(1, 1);
    c.put(2, 2);
    check(c.get(1), 1);
    c.put(3, 3);               // evicts key 2
    check(c.get(2), -1);
    c.put(4, 4);               // evicts key 1
    check(c.get(1), -1);
    check(c.get(3), 3);
    check(c.get(4), 4);

    // updating an existing key must refresh its recency and change the value
    LRUCache d(2);
    d.put(1, 1);
    d.put(2, 2);
    d.put(1, 10);              // key 1 is now most recent
    d.put(3, 3);               // evicts key 2, not 1
    check(d.get(1), 10);
    check(d.get(2), -1);

    // capacity 1
    LRUCache e(1);
    e.put(1, 1);
    e.put(2, 2);               // evicts key 1
    check(e.get(1), -1);
    check(e.get(2), 2);
    summary();
    return 0;
}
