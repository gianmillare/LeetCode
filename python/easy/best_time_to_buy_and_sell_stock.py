# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
  if len(prices) < 2:
    return 0

  sorted_list = sorted(prices, reverse=True)
  if prices == sorted_list:
    return 0 
  
  iterative_list = prices[::-1]
  results = []

  for i in iterative_list:
    for j in iterative_list[iterative_list.index(i)+1:]:
      results.append(i - j)
  
  return max(results)

# Faster Solution
def max_profit(prices):
  max_profit = 0
  min_price = float('inf')

  for price in prices:
    min_price = min(min_price, price)
    profit = price - min_price
    max_profit = max(max_profit, profit)
  return max_profit

    


prices = [7,1,5,3,6,4]
maxProfit(prices)
