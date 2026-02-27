import os
import re
import heapq

def kth_largest(nums, k):
    if not nums:
        return 
    
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heappushpop(heap, num)
    
    return heap[0]

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                # Extract cardPoints list and k value using regex
                nums_match = re.search(r"nums = \[(.*?)\]", line)
                k_match = re.search(r"k = (\d+)", line)
                
                if nums_match and k_match:
                    nums = [int(x.strip()) for x in nums_match.group(1).split(",") if x.strip()]
                    k = int(k_match.group(1))
                    result = kth_largest(nums, k)
                    print(f"nums: {nums}, k: {k} => Result: {result}")
    else:
        print(f"Error: {file_path} not found.")