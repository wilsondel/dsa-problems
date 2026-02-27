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





