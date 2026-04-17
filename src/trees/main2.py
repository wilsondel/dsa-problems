import os
import json
from typing import List


# ============================================================
# 315. Count of Smaller Numbers After Self (Hard)
# ============================================================
# Dado nums, devolvemos counts donde counts[i] = cantidad de
# elementos MENORES que nums[i] que están a la DERECHA de i.
#
# Ejemplo: nums = [5, 2, 6, 1]  =>  counts = [2, 1, 1, 0]
#
# IDEA CLAVE:
# - Recorremos el array de DERECHA a IZQUIERDA.
# - Usamos un Segment Tree indexado por VALOR (no por posición).
# - Cada hoja cuenta "cuántas veces hemos visto este valor".
#
# Para cada nums[i]:
#   1) QUERY: ¿cuántos números menores ya vimos?  -> rango [0, nums[i]-1]
#      Eso es counts[i].
#   2) UPDATE: sumamos +1 en la posición 'nums[i]' del árbol
#      (registramos que apareció).
#
# Truco práctico: como -10^4 <= nums[i] <= 10^4, DESPLAZAMOS sumando
# OFFSET = 10^4 para que todos los valores queden en [0, 20000].
# ============================================================


OFFSET = 10_000       # sumamos esto a cada valor para evitar negativos
VALUE_RANGE = 20_001  # valores posibles ya desplazados: 0..20000


class SegmentTree:
    """Segment Tree que CUENTA apariciones de valores en un rango."""

    def __init__(self, size: int):
        self.n = size
        # 4*n es el tamaño seguro estándar para un segment tree recursivo.
        self.tree = [0] * (4 * size)

    def update(self, index: int, node: int = 0, start: int = 0, end: int = -1) -> None:
        """Suma +1 a la posición 'index' (registra que vimos ese valor)."""
        if end == -1:
            end = self.n - 1

        # Caso base: llegamos a la hoja del valor.
        if start == end:
            self.tree[node] += 1
            return

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        # Bajamos por el lado donde está 'index'.
        if index <= mid:
            self.update(index, left_child, start, mid)
        else:
            self.update(index, right_child, mid + 1, end)

        # Recalculamos el conteo del nodo actual.
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, left: int, right: int, node: int = 0, start: int = 0, end: int = -1) -> int:
        """Cuenta cuántos valores hay en el rango [left, right]."""
        if end == -1:
            end = self.n - 1

        # Rango vacío (ocurre cuando nums[i] == 0 desplazado; no hay menores).
        if left > right:
            return 0

        # Caso 1: el nodo está completamente FUERA del rango pedido.
        if right < start or end < left:
            return 0

        # Caso 2: el nodo está completamente DENTRO del rango.
        if left <= start and end <= right:
            return self.tree[node]

        # Caso 3: solapamiento parcial -> preguntamos a ambos hijos.
        mid = (start + end) // 2
        left_count = self.query(left, right, 2 * node + 1, start, mid)
        right_count = self.query(left, right, 2 * node + 2, mid + 1, end)
        return left_count + right_count


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        tree = SegmentTree(VALUE_RANGE)
        result = [0] * len(nums)

        # Recorremos de DERECHA a IZQUIERDA.
        for i in range(len(nums) - 1, -1, -1):
            shifted = nums[i] + OFFSET  # desplazamos para que sea >= 0

            # ¿Cuántos valores MENORES que nums[i] ya están en el árbol?
            # Son los que están en [0, shifted - 1].
            result[i] = tree.query(0, shifted - 1)

            # Registramos la aparición de nums[i].
            tree.update(shifted)

        return result


if __name__ == "__main__":
    solution = Solution()
    file_path = os.path.join(os.path.dirname(__file__), "input2.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    nums_start = line.index("nums = ") + len("nums = ")
                    nums_end = line.index(", output = ")
                    out_start = line.index("output = ") + len("output = ")

                    nums = json.loads(line[nums_start:nums_end])
                    expected = json.loads(line[out_start:].strip())

                    result = solution.countSmaller(nums)
                    status = "✓" if result == expected else "✗"
                    print(f"{status} nums: {nums} => Result: {result}, Expected: {expected}")
                except Exception as e:
                    print(f"Error parsing line: {e}")
    else:
        print(f"Error: {file_path} not found.")
