import os
import re

def maxProfit(prices):
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                # Extract cardPoints list and k value using regex
                prices_match = re.search(r"prices = \[(.*?)\]", line)
                
                if prices_match:
                    prices = [int(x.strip()) for x in prices_match.group(1).split(",") if x.strip()]
                    result = maxProfit(prices)
                    print(f"prices: {prices} => Result: {result}")
    else:
        print(f"Error: {file_path} not found.")