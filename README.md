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
| 2026-10-06 | [19. Remove Nth Node From End of List](problems/10-linked-list/0019-remove-nth-node-from-end.cpp) | Linked list | Done |
| 2026-10-06 | [143. Reorder List](problems/10-linked-list/0143-reorder-list.cpp) | Linked list | Done |
| 2026-10-06 | [138. Copy List with Random Pointer](problems/10-linked-list/0138-copy-list-with-random-pointer.cpp) | Linked list | Done |
| 2026-10-07 | [20. Valid Parentheses](problems/11-stacks-queues/0020-valid-parentheses.cpp) | Stacks & queues | Done |
| 2026-10-11 | [21. Merge Two Sorted Lists](problems/10-linked-list/0021-merge-two-sorted-lists.cpp) | Linked list | Done |
| 2026-10-13 | [155. Min Stack](problems/11-stacks-queues/0155-min-stack.cpp) | Stacks & queues | Done |
| 2026-10-13 | [232. Implement Queue using Stacks](problems/11-stacks-queues/0232-implement-queue-using-stacks.cpp) | Stacks & queues | Done |
| 2026-10-13 | [739. Daily Temperatures](problems/11-stacks-queues/0739-daily-temperatures.cpp) | Stacks & queues | Done |
| 2026-10-14 | [146. LRU Cache](problems/10-linked-list/0146-lru-cache.cpp) | Linked list | Done |
| 2026-10-15 | [1. Two Sum](problems/02-two-pointers/0001-two-sum.py) | Hash map | Done |
| 2026-10-15 | [167. Two Sum II - Input Array Is Sorted](problems/02-two-pointers/0167-two-sum-ii-input-array-is-sorted.py) | Two pointers | Done |
| 2026-10-15 | [11. Container With Most Water](problems/02-two-pointers/0011-container-with-most-water.py) | Two pointers | Done |
| 2026-10-15 | [15. 3Sum](problems/02-two-pointers/0015-3sum.py) | Two pointers | Done |
| 2026-10-16 | [26. Remove Duplicates from Sorted Array](problems/02-two-pointers/0026-remove-duplicates-from-sorted-array.py) | Two pointers | Done |
| 2026-10-16 | [75. Sort Colors](problems/02-two-pointers/0075-sort-colors.py) | Two pointers (counting) | Done |
| 2026-10-18 | [152. Maximum Product Subarray](problems/04-kadane-subarrays/0152-maximum-product-subarray.py) | Kadane | Done |
| 2026-10-19 | [76. Minimum Window Substring](problems/03-sliding-window/0076-minimum-window-substring.py) | Sliding window | Done |
| 2026-10-19 | [918. Maximum Sum Circular Subarray](problems/04-kadane-subarrays/0918-maximum-sum-circular-subarray.py) | Kadane | Done |
| 2026-10-20 | [268. Missing Number](problems/05-cyclic-sort/0268-missing-number.py) | Cyclic sort | Done |
| 2026-10-20 | [448. Find All Numbers Disappeared in an Array](problems/05-cyclic-sort/0448-find-all-numbers-disappeared-in-an-array.py) | Cyclic sort | Done |
| 2026-10-20 | [287. Find the Duplicate Number](problems/05-cyclic-sort/0287-find-the-duplicate-number.py) | Cyclic sort | Done |

## Progress by pattern

| Pattern | Done | WIP |
|---------|------|-----|
| Prefix sum | 1 | 0 |
| Two pointers | 5 | 0 |
| Sliding window | 5 | 0 |
| Kadane / subarrays | 3 | 0 |
| Cyclic sort | 3 | 0 |
| Binary search on arrays | 0 | 0 |
| Recursion | 0 | 0 |
| Backtracking | 0 | 0 |
| Sorting & binary search | 1 | 0 |
| Linked list | 8 | 0 |
| Stacks & queues | 4 | 0 |
| Trees & BST | 0 | 0 |
| Graphs | 0 | 0 |
| Dynamic programming | 0 | 0 |
