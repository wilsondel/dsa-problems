# DSA Problems

## Two Pointers

### Valid Triangle Number (Medium)

**Description**  
Count the number of triplets in an array that can form a valid triangle.

**The Rule:**  
Three sides `a`, `b`, and `c` form a triangle if:
> **a + b > c** (where `c` is the longest side)

---

### 💡 The Strategy: Sort & Shrink

By sorting the array, we only need to check one condition: **Smallest + Middle > Largest**.

#### The Step-by-Step Logic:
1.  **Sort the array:** This helps us identify the largest side (`c`) easily.
2.  **Fix the Largest Side:** We loop backwards through the array. The current number is our potential longest side `c`.
3.  **Two Pointers:** For each `c`, we place:
    *   `left` at the very beginning (the smallest side).
    *   `right` just before `c` (the middle side).
4.  **The Shortcut:**
    *   **If `nums[left] + nums[right] > c`:** 
        Since the array is sorted, if the smallest side (`left`) works, then **every side between `left` and `right`** will also work with `right` and `c`!
        *   We add them all at once: `count += (right - left)`.
        *   Move `right` down to try a different middle side.
    *   **If `nums[left] + nums[right] <= c`:**
        The sum is too small. Move `left` up to increase the sum.

**Example:** `nums = [11, 4, 9, 6, 15, 18]`
1.  Sorted: `[4, 6, 9, 11, 15, 18]`
2.  Fix `c = 18`. `left = 4`, `right = 15`.
3.  `4 + 15 = 19`. `19 > 18`? **Yes!**
4.  Everything between index 0 and 4 works. Triplets: `(4,15,18), (6,15,18), (9,15,18), (11,15,18)`.
5.  `count += 4`.

---
## Sliding Window

### Max Points You Can Obtain From Cards (Medium)

**Description**  
Given an array of integers representing card values, calculate the maximum score you can achieve by picking exactly **k** cards.

**Rules:**
*   You must pick cards in order from **either end** (left or right).
*   You can take some from the start and some from the end.
*   You **cannot** skip cards or pick from the middle.

**Example 1:**
*   `cards = [2, 11, 4, 5, 3, 9, 2]`, `k = 3`
*   **Output:** `17`
*   **Explanation:** Taking the first 3 cards (`2 + 11 + 4`) gives 17, which is the maximum possible.

**Example 2:**
*   `cards = [1, 100, 10, 0, 4, 5, 6]`, `k = 3`
*   **Output:** `111`
*   **Explanation:** Take the first 3 cards (`1 + 100 + 10 = 111`).

---

### 💡 The Simple Logic: "What's Left Behind?"

The trick to solving this easily is to look at what you **don't** pick.

If you pick **k** cards from the ends, you are leaving behind a consecutive "window" of **n - k** cards in the middle.

**Example:** `cards = [2, 11, 4, 5, 3, 9, 2]` (7 cards total), `k = 3`
*   You pick 3 cards.
*   You leave behind **4** cards (7 - 3 = 4).

Every way to pick 3 cards from the ends matches a specific window of 4 cards in the middle:
*   Pick `[2, 11, 4]` (Start) $\rightarrow$ Leave `[5, 3, 9, 2]` (Middle/End)
*   Pick `[9, 2, 2]` (End/Start) $\rightarrow$ Leave `[11, 4, 5, 3]` (Middle)

### Why This Matters
Since we know the **Total Sum** of all cards:
> **Sum of Picked Cards** = **Total Sum** - **Sum of Unpicked Cards**

To get the **Maximum** score for the cards we pick, we just need to find the **Minimum** sum of the cards we leave behind!

### The Algorithm
1.  Calculate the `total_sum` of all cards.
2.  Use a **fixed-length sliding window** of size `n - k`.
3.  Slide this window across the array to find the **min window sum**.
4.  `Max Score = total_sum - min_window_sum`.

This transforms a complex "pick from both ends" problem into a simple "find the smallest middle" problem.

---
## Heap

### Kth Largest Element in an Array (Medium)

**Description**  
Find the **k-th** largest element in an unsorted array. Note that it is the k-th largest element in the sorted order, not the k-th distinct element.

**Example:**
*   `nums = [3, 2, 1, 5, 6, 4]`, `k = 2`
*   **Output:** `5`

---

### 💡 The Strategy: Min-Heap of Size K

To find the $k$-th largest element efficiently, we don't need to sort the entire array. We only need to keep track of the **top $k$** largest numbers we've seen.

The best tool for this is a **Min-Heap**.

#### The Step-by-Step Logic:
1.  **Maintain a small "club":** We create a Min-Heap that will only hold **k** elements.
2.  **Fill the heap:** Add numbers from the array one by one.
3.  **Keep the strongest:** If the heap already has `k` elements and we find a new number that is **larger** than the smallest one in our heap (the one at the top):
    *   We remove the smallest element.
    *   We add the new, larger number.
4.  **The Result:** After looking at every number, the heap contains the $k$ largest elements of the array. Since it's a Min-Heap, the **smallest** of these $k$ elements is sitting right at the top. That smallest element is exactly the $k$-th largest!

**Why use a Min-Heap?**  
A Min-Heap makes it very fast to see the smallest element ($O(1)$) and fast to replace it ($O(\log k)$). This is much more efficient than sorting the whole array ($O(n \log n)$) when $k$ is small.

---
## Greedy

### Best Time to Buy and Sell Stock (Easy)

**Description**  
You are given an array `prices` where `prices[i]` is the price of a given stock on the $i^{th}$ day. You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

**Example:**
*   `prices = [7, 1, 5, 3, 6, 4]`
*   **Output:** `5`
*   **Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = $6-1 = 5$.

---

### 💡 The Strategy: One Pass (Greedy)

The simplest way to solve this is to imagine you are walking through the timeline of prices and keeping track of the best deal you've seen so far.

#### The Step-by-Step Logic:
1.  **Look for the Floor:** As you go through the prices, keep track of the **lowest price** you have encountered so far (`min_price`).
2.  **Calculate the "What If":** For every new price you see, ask yourself: *"If I bought at my lowest price and sold today, how much money would I make?"*
3.  **Remember the Record:** Keep track of the **highest profit** you've calculated so far.
4.  **Keep Moving:** You only need to look at each price once!

**Why is this "Greedy"?**  
At every step, you are making the best possible decision based on what you've seen (updating the minimum price) and recording the best possible outcome found so far (maximum profit).

---
## Dynamic Programming

### Unique Paths (Medium)

**Description**  
You are given a robot that starts at the top-left corner of a grid with dimensions **m x n**. The robot can only move either down or right at any point in time. The goal is for the robot to reach the bottom-right corner of the grid.

Given the dimensions of the board **m** and **n**, write a function to return the number of unique paths the robot can take to reach the bottom-right corner.

**Example:**
*   `m = 3`, `n = 2`
*   **Output:** `3`
*   **Explanation:** From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down

---

### 💡 The Strategy: Top-Down DP (Memoization)

This problem can be broken down into smaller sub-problems. To reach any cell `(i, j)`, you must have come from either the cell above it `(i-1, j)` or the cell to its left `(i, j-1)`.

#### The Step-by-Step Logic:
1.  **Base Case:** If you are in the first row (`m=1`) or the first column (`n=1`), there is only **1** way to reach any cell (by going straight right or straight down).
2.  **Recursive Relation:** The number of ways to reach `(m, n)` is the sum of the ways to reach the cell above it and the cell to its left:
    > `paths(m, n) = paths(m-1, n) + paths(m, n-1)`
3.  **Memoization:** To avoid recalculating the same paths multiple times (which would be very slow), we store for each `(m, n)` in a **dictionary (`memo`)**.
4.  **Lookup:** Before calculating a path for `(m, n)`, check if it is already in the `memo`. If it is, return it immediately!

**Why use Dynamic Programming?**  
A simple recursive solution would have an exponential time complexity of $O(2^{m+n})$. With **Memoization**, we calculate each cell's unique paths exactly once, reducing the complexity to $O(m \times n)$, which is significantly faster for larger grids.

---

### Distinct Subsequences (Hard)

**Description**  
Given two strings `s` and `t`, return the number of distinct subsequences of `s` which equals `t`.

**Example:**
*   `s = "rabbbit"`, `t = "rabbit"`
*   **Output:** `3`
*   **Explanation:** There are 3 ways to generate "rabbit" from `s` by picking different 'b's.

---

### 💡 The Strategy: Decision Tree with Memoization

To solve this, we explore all possible ways to form `t` from `s` using a recursive approach (DFS). At each step, we decide whether to include a character from `s` in our subsequence.

#### The Step-by-Step Logic:
1.  **The Goal:** We use two pointers, `i` for string `s` and `j` for string `t`.
2.  **Base Cases:**
    *   If `j` reaches the end of `t`, we found a valid subsequence! Return **1**.
    *   If `i` reaches the end of `s` but `j` hasn't finished `t`, this path failed. Return **0**.
3.  **The Decision:**
    *   **Always skip:** We can always choose to skip `s[i]` and try to find `t[j]` later in `s`.
    *   **Match & Include:** If `s[i] == t[j]`, we have an *additional* option: include `s[i]` and move both pointers forward (`i+1`, `j+1`).
4.  **Memoization:** We store the results of `(i, j)` in a `cache` dictionary to avoid repeating the same sub-problems.

**Why use this approach?**  
Without memoization, the number of paths grows exponentially. By caching the results, we ensure that each pair of indices `(i, j)` is computed only once, leading to a time complexity of $O(n \times m)$, where $n$ and $m$ are the lengths of the strings.

---
## Breadth-First Search

### Rightmost Node (Medium)

**Description**  
Given the root of a binary tree, return the rightmost node at each level of the tree. The output should be a list containing only the values of those nodes.

**Example 1:**
*   **Input:** `[1, 3, 4, null, 2, 7, null, 8]`
*   **Output:** `[1, 4, 7, 8]`

**Example 2:**
*   **Input:** `[1, 2, 5, 3, null, null, 4]`
*   **Output:** `[1, 5, 3, 4]`

---

### 💡 The Strategy: Level-Order Traversal (BFS)

To find the rightmost node at each level, we explore the tree level by level. At each level, the last node we visit is the one that would be visible from the right.

#### The Step-by-Step Logic:
1.  **Queue for Traversal:** Use a queue to keep track of nodes to visit, starting with the `root`.
2.  **Level by Level:** While the queue is not empty:
    *   Record the number of nodes at the current level (`level_size`).
    *   Iterate through these nodes one by one.
3.  **Identify the Rightmost:** For each level, the **last node** in the iteration is the rightmost node. Add its value to our result list.
4.  **Add Children:** As we visit each node, add its `left` and `right` children (if they exist) to the queue for the next level.

**Why use BFS?**  
Breadth-First Search is ideal here because it naturally groups nodes by their depth. By processing an entire level before moving to the next, we can easily identify which node is at the "end" of that level.
