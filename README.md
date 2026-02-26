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
3.  Slide this window across the array to find the **minimum window sum**.
4.  `Max Score = total_sum - min_window_sum`.

This transforms a complex "pick from both ends" problem into a simple "find the smallest middle" problem.





