# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/
# Pattern : graph traversal + hashmap (old node -> its clone)
# Time    : O(V + E)      Space: O(V)
# Solved  : 2026-11-18

from collections import deque
from typing import Optional


# ---- test helper: one PASS/FAIL line per case + a summary at the end ----
tests_run = tests_passed = 0


def check(got, expected):
    global tests_run, tests_passed
    tests_run += 1
    if got == expected:
        tests_passed += 1
        print(f"✅ PASS #{tests_run}")
    else:
        print(f"❌ FAIL #{tests_run}  got {got}, expected {expected}")


def summary():
    ok = tests_passed == tests_run
    print(f"\n{tests_passed}/{tests_run}  {'✅ ALL PASSED' if ok else '❌ SOME FAILED'}")
# -------------------------------------------------------------------------


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        # return a DEEP COPY: brand-new Node objects with the same connections

        # 1. empty graph: nothing to clone
        if node is None:
            return None

        # 2. old node -> its clone. Doubles as the "visited" check:
        #    if a node is in here, it has already been cloned.
        clones = {}

        # 3. dfs(old) returns the clone of `old`
        def dfs(old):
            # a. already cloned? reuse it (this stops infinite loops on cycles)
            if old in clones:
                return clones[old]

            # b. make the clone (same value, empty neighbors for now) and
            #    store it BEFORE visiting neighbors, so a cycle that comes
            #    back to `old` finds it in the dict
            clone = Node(old.val)
            clones[old] = clone

            # c. clone every neighbor and connect it to this clone
            for nei in old.neighbors:
                clone.neighbors.append(dfs(nei))

            # d. hand the finished clone back to the caller
            return clone

        # 4. start from the node we were given
        return dfs(node)


# ---- helpers to build and inspect graphs for the tests ----
def build_graph(adj):
    """adj[i] = neighbor values of node i+1 (LeetCode format). Returns node 1, or None."""
    if not adj:
        return None
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, nbrs in enumerate(adj):
        nodes[i].neighbors = [nodes[j - 1] for j in nbrs]
    return nodes[0]


def all_nodes(start):
    """Every node reachable from start, as a list."""
    if start is None:
        return []
    seen = {start}
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        for nei in cur.neighbors:
            if nei not in seen:
                seen.add(nei)
                queue.append(nei)
    return list(seen)


def to_adj(start):
    """Turn a graph back into LeetCode's adjacency-list format."""
    nodes = {n.val: n for n in all_nodes(start)}
    return [[nb.val for nb in nodes[v].neighbors] for v in sorted(nodes)]


def shares_nodes(orig, clone):
    """True if the clone reuses any original Node object (that would be a shallow copy)."""
    return bool({id(n) for n in all_nodes(orig)} & {id(n) for n in all_nodes(clone)})
# -----------------------------------------------------------


if __name__ == "__main__":
    s = Solution()
    cases = [
        [[2, 4], [1, 3], [2, 4], [1, 3]],   # square of 4 nodes
        [[]],                                # single node, no neighbors
        [],                                  # empty graph
        [[2], [1]],                          # two nodes
    ]
    for adj in cases:
        original = build_graph(adj)
        clone = s.cloneGraph(original)
        check(to_adj(clone), adj)                     # same structure
        check(shares_nodes(original, clone), False)   # but all-new nodes
    summary()
