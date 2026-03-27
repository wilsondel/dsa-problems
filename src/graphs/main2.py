import os
import re
from collections import deque
from typing import List


class Solution:
    def bus_routes(self, routes, source, target):
        if source == target:
            return 0

        # Create a dictionary mapping bus stop to bus route index
        bus_stops = {}
        for i, route in enumerate(routes):
            for stop in route:
                if stop not in bus_stops:
                    bus_stops[stop] = []
                bus_stops[stop].append(i)

        visited = set()
        queue = deque()

        # Initialize BFS queue and visited set
        for bus in bus_stops[source]:
            queue.append((bus, 1))
            visited.add(bus)

        while queue:
            curr_bus, num_changes = queue.popleft()

            for stop in routes[curr_bus]:
                if stop == target:
                    return num_changes

                for connected_bus in bus_stops[stop]:
                    if connected_bus not in visited:
                        queue.append((connected_bus, num_changes + 1))
                        visited.add(connected_bus)

        return -1


if __name__ == "__main__":
    solution = Solution()
    file_path = os.path.join(os.path.dirname(__file__), "input2.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue

                # Parse routes: extract all [...] groups, first one is routes (may have nested lists)
                routes_match = re.search(r"routes = (\[\[.*\]\])", line)
                source_match = re.search(r"source = (\d+)", line)
                target_match = re.search(r"target = (\d+)", line)
                output_match = re.search(r"output = (-?\d+)", line)

                if routes_match and source_match and target_match and output_match:
                    routes = [
                        [int(x) for x in group.split(",")]
                        for group in re.findall(r"\[([^\[\]]+)\]", routes_match.group(1))
                    ]
                    source = int(source_match.group(1))
                    target = int(target_match.group(1))
                    expected = int(output_match.group(1))

                    result = solution.bus_routes(routes, source, target)
                    status = "✓" if result == expected else "✗"
                    print(f"{status} routes={routes}, source={source}, target={target} => Result: {result}, Expected: {expected}")
    else:
        print(f"Error: {file_path} not found.")