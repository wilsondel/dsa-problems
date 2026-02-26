import os
import re


def maxScore(cards, k):
  total = sum(cards)
  if k == len(cards):
    return total
  state = 0
  max_points = 0
  start = 0
  for end in range(len(cards)):
    state += cards[end]
    if end - start + 1 == len(cards) - k:
      max_points = max(total - state, max_points)
      state -= cards[start]
      start += 1
  return max_points

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                # Extract cardPoints list and k value using regex
                cards_match = re.search(r"cardPoints = \[(.*?)\]", line)
                k_match = re.search(r"k = (\d+)", line)
                
                if cards_match and k_match:
                    cards = [int(x.strip()) for x in cards_match.group(1).split(",") if x.strip()]
                    k = int(k_match.group(1))
                    result = maxScore(cards, k)
                    print(f"Cards: {cards}, k: {k} => Result: {result}")
    else:
        print(f"Error: {file_path} not found.")