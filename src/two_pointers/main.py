import os
import re


def triangleNumber(nums):
    nums.sort()
    
    count = 0
    for i in range(len(nums) - 1, 1, -1):
        left = 0
        right = i - 1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                count += right - left
                right -= 1
            else:
                left += 1
    
    return count

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                # Extract nums list using regex
                nums_match = re.search(r"nums = \[(.*?)\]", line)
                
                if nums_match:
                    nums = [int(x.strip()) for x in nums_match.group(1).split(",") if x.strip()]
                    result = triangleNumber(nums)
                    print(f"nums: {nums} => Result: {result}")
    else:
        print(f"Error: {file_path} not found.")