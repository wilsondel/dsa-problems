import os
import re


def numDistinct(s: str, t: str) -> int:
    cache = {}

    def dfs(i, j):
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        
        if (i, j) in cache:
            return cache[(i, j)]
        
        # Opción 1: Siempre podemos saltar el caracter actual de 's'
        res = dfs(i + 1, j)
        
        # Opción 2: Si los caracteres coinciden, sumamos las posibilidades de usarlo
        if s[i] == t[j]:
            res += dfs(i + 1, j + 1)
            
        cache[(i, j)] = res
        return res
    
    return dfs(0, 0)

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "input2.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                match = re.search(r"s = \"(\w+)\", t = \"(\w+)\"", line)
                if match:
                    s = match.group(1)
                    t = match.group(2)
                    result = numDistinct(s, t)
                    print(f"s: {s}, t: {t} => Result: {result}")
    else:
        print(f"Error: {file_path} not found.")