# brute-to-better

Brute force first, then optimize. Daily DSA practice in C++, organised by pattern.

## Structure

```
problems/
  01-prefix-sum/
  02-two-pointers/
  03-sliding-window/
  04-kadane-subarrays/
  05-cyclic-sort/
  06-binary-search-arrays/
  07-recursion/
  08-backtracking/
  09-sorting-binary-search/
  10-linked-list/
  11-stacks-queues/
  12-trees-bst/
  13-graphs/
  14-dynamic-programming/
templates/
  solution_template.cpp   copy this to start a new problem
```

One file per problem: `<lc-number>-<slug>.cpp`, with a header (link, pattern, complexity, date).
Where useful, a file keeps both the brute-force and the optimized version.

Compile and run any solution:
```
g++ -std=c++17 -o /tmp/sol problems/<pattern>/<file>.cpp && /tmp/sol
```

## Streak log

One row per day, newest at the bottom.

| Date       | Problem | Pattern | Status |
|------------|---------|---------|--------|
| 2026-09-12 | [15. 3Sum](problems/02-two-pointers/0015-3sum.cpp) | Two pointers | WIP |
| 2026-09-22 | [2461. Max Sum of Distinct Subarrays With Length K](problems/03-sliding-window/2461-max-sum-distinct-subarrays-k.cpp) | Sliding window | Done |
| 2026-09-23 | [3. Longest Substring Without Repeating Characters](problems/03-sliding-window/0003-longest-substring-no-repeat.cpp) | Sliding window | Done |
| 2026-09-24 | [904. Fruit Into Baskets](problems/03-sliding-window/0904-fruit-into-baskets.cpp) | Sliding window | Done |
| 2026-09-24 | [53. Maximum Subarray](problems/04-kadane-subarrays/0053-maximum-subarray.cpp) | Kadane | Done |
| 2026-09-30 | [560. Subarray Sum Equals K](problems/01-prefix-sum/0560-subarray-sum-equals-k.cpp) | Prefix sum | Done |
| 2026-09-30 | [724. Find Pivot Index](problems/01-prefix-sum/0724-find-pivot-index.cpp) | Prefix sum | Done |
| 2026-10-03 | [875. Koko Eating Bananas](problems/09-sorting-binary-search/0875-koko-eating-bananas.cpp) | Sorting & binary search | Done |
| 2026-10-04 | [1004. Max Consecutive Ones III](problems/03-sliding-window/1004-max-consecutive-ones-iii.cpp) | Sliding window | Done |
| 2026-10-04 | [206. Reverse Linked List](problems/10-linked-list/0206-reverse-linked-list.cpp) | Linked list | Done |
| 2026-10-05 | [141. Linked List Cycle](problems/10-linked-list/0141-linked-list-cycle.cpp) | Linked list | Done |
| 2026-10-05 | [876. Middle of the Linked List](problems/10-linked-list/0876-middle-of-the-linked-list.cpp) | Linked list | Done |

## Progress by pattern

| Pattern | Done | WIP |
|---------|------|-----|
| Prefix sum | 1 | 0 |
| Two pointers | 0 | 1 |
| Sliding window | 4 | 0 |
| Kadane / subarrays | 1 | 0 |
| Cyclic sort | 0 | 0 |
| Binary search on arrays | 0 | 0 |
| Recursion | 0 | 0 |
| Backtracking | 0 | 0 |
| Sorting & binary search | 1 | 0 |
| Linked list | 3 | 0 |
| Stacks & queues | 0 | 0 |
| Trees & BST | 0 | 0 |
| Graphs | 0 | 0 |
| Dynamic programming | 0 | 0 |
