import os
import re
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(nums):
    if not nums or nums[0] is None:
        return None
    root = TreeNode(nums[0])
    queue = deque([root])
    i = 1
    while queue and i < len(nums):
        node = queue.popleft()
        if i < len(nums):
            if nums[i] is not None:
                node.left = TreeNode(nums[i])
                queue.append(node.left)
            i += 1
        if i < len(nums):
            if nums[i] is not None:
                node.right = TreeNode(nums[i])
                queue.append(node.right)
            i += 1
    return root


class Solution:
    def rightmostNode(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        nodes = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # current node is the rightmost node
                if i == level_size - 1:
                    nodes.append(node.val)

                # add nodes as normal to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return nodes


if __name__ == "__main__":
    solution = Solution()
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                nums_match = re.search(r"input = \[(.*?)\]", line)
                output_match = re.search(r"output = \[(.*?)\]", line)

                if nums_match and output_match:
                    nums = [int(x.strip()) if x.strip() != 'null' else None for x in nums_match.group(1).split(",") if x.strip()]
                    expected = [int(x.strip()) for x in output_match.group(1).split(",") if x.strip()]
                    root = buildTree(nums)
                    result = solution.rightmostNode(root)
                    status = "✓" if result == expected else "✗"
                    print(f"{status} input: {nums} => Result: {result}, Expected: {expected}")
    else:
        print(f"Error: {file_path} not found.")