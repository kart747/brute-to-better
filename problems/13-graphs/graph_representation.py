from collections import deque

# Graph representation: adjacency list from an edge list
# Practice: write it twice from memory (Graphs 1 warm-up)


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


def build_undirected(n: int, edges: list[list[int]]) -> list[list[int]]:
    # write it here (pass 1)
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def build_directed(n: int, edges: list[list[int]]) -> list[list[int]]:
    # write it here (pass 2, from memory)
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
    return graph


def bfs(graph, start):
    visited = [False] * len(graph)
    visited[start] = True              # mark when you PUSH
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in graph[node]:
            if not visited[nei]:
                visited[nei] = True
                queue.append(nei)
    return order


def dfs(graph, start):
    visited = [False] * len(graph)
    order = []

    def go(node):
        visited[node] = True
        order.append(node)
        for nei in graph[node]:
            if not visited[nei]:
                go(nei)

    go(start)
    return order


if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
    check(build_undirected(5, edges), [[1, 2], [0, 3], [0, 3], [1, 2, 4], [3]])
    check(build_directed(5, edges), [[1, 2], [3], [3], [4], []])
    check(build_undirected(3, []), [[], [], []])      # no edges
    check(build_undirected(1, []), [[]])              # single node

    g = build_undirected(5, edges)
    check(bfs(g, 0), [0, 1, 2, 3, 4])
    check(dfs(g, 0), [0, 1, 3, 2, 4])
    summary()
