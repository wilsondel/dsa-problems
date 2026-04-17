import os
import json
from typing import List


# ============================================================
# SEGMENT TREE - Explicación rápida
# ============================================================
# Un Segment Tree es un árbol binario donde cada nodo guarda
# información (en este caso, la SUMA) de un rango del array.
#
# Ejemplo con nums = [1, 3, 5, 7]:
#
#                    [0..3] sum=16
#                   /            \
#            [0..1] sum=4      [2..3] sum=12
#             /     \            /      \
#        [0]=1   [1]=3       [2]=5    [3]=7
#
# - La RAÍZ cubre todo el array.
# - Cada nodo se divide en dos mitades hasta llegar a las hojas
#   (un solo elemento del array).
# - Para consultar un rango, combinamos solo los nodos necesarios.
# - Para actualizar un valor, recorremos desde la hoja hasta la raíz.
#
# Complejidad: update y sumRange en O(log n).
# ============================================================


class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        # Reservamos 4*n espacio: suficiente para cualquier árbol binario
        # que represente un array de n elementos (regla práctica segura).
        self.tree = [0] * (4 * self.n)
        # Construimos el árbol empezando en el nodo 0, cubriendo [0, n-1].
        self._build(nums, node=0, start=0, end=self.n - 1)

    def _build(self, nums, node, start, end):
        """Construye el árbol de forma recursiva.
        - node: índice actual en el array self.tree
        - start, end: rango del array original que este nodo representa
        """
        # Caso base: el nodo representa un solo elemento (hoja).
        if start == end:
            self.tree[node] = nums[start]
            return

        # Dividimos el rango en dos mitades.
        mid = (start + end) // 2
        left_child = 2 * node + 1   # hijo izquierdo
        right_child = 2 * node + 2  # hijo derecho

        # Construimos recursivamente cada mitad.
        self._build(nums, left_child, start, mid)
        self._build(nums, right_child, mid + 1, end)

        # El valor del nodo actual es la suma de sus dos hijos.
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, index: int, val: int) -> None:
        """Actualiza nums[index] = val y propaga el cambio hacia arriba."""
        self._update(node=0, start=0, end=self.n - 1, index=index, val=val)

    def _update(self, node, start, end, index, val):
        # Caso base: encontramos la hoja correspondiente a 'index'.
        if start == end:
            self.tree[node] = val
            return

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        # Decidimos en qué mitad está 'index' y bajamos por ese lado.
        if index <= mid:
            self._update(left_child, start, mid, index, val)
        else:
            self._update(right_child, mid + 1, end, index, val)

        # Al volver de la recursión, recalculamos la suma del nodo actual.
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def sumRange(self, left: int, right: int) -> int:
        """Suma los elementos del array en el rango [left, right]."""
        return self._query(node=0, start=0, end=self.n - 1, left=left, right=right)

    def _query(self, node, start, end, left, right):
        # Caso 1: el rango del nodo está completamente FUERA del rango pedido.
        # No aporta nada, devolvemos 0.
        if right < start or end < left:
            return 0

        # Caso 2: el rango del nodo está completamente DENTRO del rango pedido.
        # Todo este segmento cuenta, devolvemos su suma ya calculada.
        if left <= start and end <= right:
            return self.tree[node]

        # Caso 3: hay solapamiento parcial. Preguntamos a ambos hijos y sumamos.
        mid = (start + end) // 2
        left_sum = self._query(2 * node + 1, start, mid, left, right)
        right_sum = self._query(2 * node + 2, mid + 1, end, left, right)
        return left_sum + right_sum


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    ops_start = line.index("ops = ") + len("ops = ")
                    ops_end = line.index(", args = ")
                    args_start = line.index("args = ") + len("args = ")
                    args_end = line.index(", output = ")
                    out_start = line.index("output = ") + len("output = ")

                    ops = json.loads(line[ops_start:ops_end])
                    args = json.loads(line[args_start:args_end])
                    expected = json.loads(line[out_start:].strip())

                    num_array = None
                    results = []
                    for op, arg in zip(ops, args):
                        if op == "NumArray":
                            num_array = NumArray(arg[0])
                            results.append(None)
                        elif op == "update":
                            num_array.update(arg[0], arg[1])
                            results.append(None)
                        elif op == "sumRange":
                            results.append(num_array.sumRange(arg[0], arg[1]))

                    status = "✓" if results == expected else "✗"
                    print(f"{status} ops: {ops} => Result: {results}, Expected: {expected}")
                except Exception as e:
                    print(f"Error parsing line: {e}")
    else:
        print(f"Error: {file_path} not found.")
