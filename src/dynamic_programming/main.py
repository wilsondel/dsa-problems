import os
import re


def uniquePaths(m: int, n: int, memo: dict = {}) -> int:
    if m == 1 or n == 1:
        return 1
    elif (m, n) in memo:
        return memo[(m, n)]
    else:
        memo[(m, n)] = uniquePaths(m - 1, n, memo) + uniquePaths(m, n - 1, memo)
        return memo[(m, n)]

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                match = re.search(r"m = (\d+), n = (\d+)", line)
                if match:
                    m = int(match.group(1))
                    n = int(match.group(2))
                    result = uniquePaths(m, n)
                    print(f"m: {m}, n: {n} => Result: {result}")
    else:
        print(f"Error: {file_path} not found.")