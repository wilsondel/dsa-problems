# DSA Problems

## Two Pointers
Triangle Numbers

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





