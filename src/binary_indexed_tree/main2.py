import os
import re
import json
import bisect
from typing import List


# ============================================================
# BIT - Reverse Pairs
# ============================================================
# Count pairs (i, j) with i < j and nums[i] > 2 * nums[j].
#
# Traverse RIGHT to LEFT. For each nums[i], query how many
# elements already in the BIT satisfy 2x < nums[i],
# i.e. x <= (nums[i] - 1) // 2.
#
# Values can be negative and up to ±2^31, so we use
# COORDINATE COMPRESSION:
#   sorted_vals: unique values of nums, sorted
#   rank[v]:     1-based position of v in sorted_vals
#
# The query uses bisect_right to translate the threshold
# into a rank range, avoiding a huge BIT.
#
# Complexity: O(n log n) — compression + BIT pass.
# ============================================================


def reversePairs(nums: List[int]) -> int:
    sorted_vals = sorted(set(nums))
    m = len(sorted_vals)
    rank = {v: i + 1 for i, v in enumerate(sorted_vals)}  # 1-based

    tree = [0] * (m + 1)

    def update(r: int) -> None:
        while r <= m:
            tree[r] += 1
            r += r & (-r)

    def query(r: int) -> int:
        s = 0
        while r > 0:
            s += tree[r]
            r -= r & (-r)
        return s

    count = 0
    for num in reversed(nums):
        # find x such that 2x < num, i.e. x <= (num-1)//2
        # bisect_right returns the first rank whose value > threshold
        threshold = (num - 1) // 2
        r = bisect.bisect_right(sorted_vals, threshold)
        count += query(r)
        update(rank[num])

    return count


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "input2.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    nums_match = re.search(r"nums = (\[.*?\])", line)
                    expected_match = re.search(r"output = (\d+)", line)
                    nums = json.loads(nums_match.group(1))
                    expected = int(expected_match.group(1))
                    result = reversePairs(nums)
                    status = "✓" if result == expected else "✗"
                    print(f"{status} nums: {nums} => Result: {result}, Expected: {expected}")
                except Exception as e:
                    print(f"Error parsing line: {e}")
    else:
        print(f"Error: {file_path} not found.")
