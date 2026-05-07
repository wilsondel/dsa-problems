import os
import re
import json
from typing import List


# ============================================================
# BIT - Count Number of Teams
# ============================================================
# Para cada soldado j (elemento del medio), contamos:
#   left_smaller[j]:  elementos a su IZQUIERDA con rating menor
#   left_larger[j]:   elementos a su IZQUIERDA con rating mayor
#   right_smaller[j]: elementos a su DERECHA  con rating menor
#   right_larger[j]:  elementos a su DERECHA  con rating mayor
#
# Aporte de j como elemento del medio:
#   ascendente:  left_smaller[j] * right_larger[j]
#   descendente: left_larger[j]  * right_smaller[j]
#
# El BIT está indexado por RATING (1..10^5, todos únicos).
# Dos pasadas: izquierda→derecha y derecha→izquierda.
# Complejidad: O(n log M) donde M = 10^5.
# ============================================================

MAX_RATING = 100000


def numTeams(rating: List[int]) -> int:
    n = len(rating)

    def update(tree: List[int], i: int) -> None:
        while i <= MAX_RATING:
            tree[i] += 1
            i += i & (-i)

    def query(tree: List[int], i: int) -> int:
        s = 0
        while i > 0:
            s += tree[i]
            i -= i & (-i)
        return s

    left_smaller = [0] * n
    left_larger = [0] * n
    right_smaller = [0] * n
    right_larger = [0] * n

    tree = [0] * (MAX_RATING + 1)
    for j in range(n):
        left_smaller[j] = query(tree, rating[j] - 1)
        left_larger[j] = j - query(tree, rating[j])
        update(tree, rating[j])

    tree = [0] * (MAX_RATING + 1)
    for j in range(n - 1, -1, -1):
        right_smaller[j] = query(tree, rating[j] - 1)
        right_larger[j] = (n - 1 - j) - query(tree, rating[j])
        update(tree, rating[j])

    return sum(
        left_smaller[j] * right_larger[j] + left_larger[j] * right_smaller[j]
        for j in range(n)
    )


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    rating_match = re.search(r"rating = (\[.*?\])", line)
                    expected_match = re.search(r"output = (\d+)", line)
                    rating = json.loads(rating_match.group(1))
                    expected = int(expected_match.group(1))
                    result = numTeams(rating)
                    status = "✓" if result == expected else "✗"
                    print(f"{status} rating: {rating} => Result: {result}, Expected: {expected}")
                except Exception as e:
                    print(f"Error parsing line: {e}")
    else:
        print(f"Error: {file_path} not found.")
