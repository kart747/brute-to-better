# DSA

My data structures & algorithms practice, organised by pattern. Language: C++.

## Structure

```
problems/
  <pattern>/            e.g. sliding-window, two-pointers, dp, graphs ...
    <number>-<slug>.cpp one file per problem, with header (link, pattern, complexity)
templates/
  solution_template.cpp copy this to start a new problem
```

Compile and run any solution: `g++ -std=c++17 -o /tmp/sol problems/<pattern>/<file>.cpp && /tmp/sol`

## Streak log

Add one row per day, newest at the bottom.

| Date       | Problem                                              | Pattern        | Status |
|------------|------------------------------------------------------|----------------|--------|
| 2026-09-12 | [15. 3Sum](problems/two-pointers/0015-3sum.cpp)      | Two pointers   | WIP    |
| 2026-09-22 | [2461. Max Sum of Distinct Subarrays With Length K](problems/sliding-window/2461-max-sum-distinct-subarrays-k.cpp) | Sliding window | Done   |

## Patterns covered

| Pattern        | Solved |
|----------------|--------|
| Sliding window | 1      |
| Two pointers   | 0 (1 WIP) |
