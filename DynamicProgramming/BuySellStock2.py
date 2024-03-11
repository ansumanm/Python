"""
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/ --> maxProfit
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/ --> maxProfit3
"""

from typing import List

class Solution:
	def max1Generator(self, prices: List[int]):
		maxP = 0
		buyPrice = prices[0]
		profits = [0] * len(prices)
		for i in range(0, len(prices)):
			price = prices[i]
			sellPrice = price
			maxP = max(maxP, sellPrice - buyPrice)
			if buyPrice > sellPrice:
				buyPrice = sellPrice
			profits[i] = maxP
		
		for profit in profits:
			yield profit

			
	def max2Generator(self, prices: List[int]):
		"""
			Calculate incrementally from reverse.
			Store the result in a list,
			and return the element from the list one by one.
		Args:
			prices (List[int]): List of prices
		"""
		# Initialize the profits array.
		# d[i] represents profit from i to end date.
		profits = [0] * len(prices)
		maxP = 0

		sellPrice = prices[-1]
		for index in range(len(prices) - 1, -1, -1):
			buyPrice = prices[index]
			maxP = max(maxP, sellPrice - buyPrice)
			if buyPrice > sellPrice:
				sellPrice = buyPrice
			profits[index] = maxP

		for profit in profits:
			yield profit

			
	def maxProfit5(self, prices: List[int]) -> int:
		"""Memory and time optimized

		Args:
			prices (List[int]): List of prices

		Returns:
			int: max profit in 2 transactions.
		"""
		maxP = 0
		max1Gen = self.max1Generator(prices)
		max2Gen = self.max2Generator(prices)
		for _ in range(0, len(prices)):
			max1 = next(max1Gen)
			max2 = next(max2Gen)
			print(f"max1 {max1} max2 {max2} maxP {maxP}")
			maxP = max(maxP, max1 + max2)

		return maxP

	def maxP(self, prices: List[int]) -> int:
		"""Memory optimized solution. Dont maintain an array of profits. Instead compute it on fly.

		Args:
			prices (List[int]): List of prices

		Returns:
			int: Returns max profit
		"""
		if not prices:
			return 0

		maxProfit = 0
		index = 0
		buyPrice = prices[0]

		while index < len(prices):
			sellPrice = prices[index]
			maxProfit = max(maxProfit, sellPrice - buyPrice)
			if sellPrice < buyPrice:
				buyPrice = sellPrice
			index += 1
    
		return maxProfit


	def maxProfit4(self, prices: List[int]) -> int:
		maxProfit = 0
		for day_index in range(0, len(prices)):
			max1 = self.maxP(prices[0:day_index])
			max2 = self.maxP(prices[day_index:len(prices)])
			maxProfit = max(maxProfit, max1 + max2)

		return maxProfit


	def maxProfit3(self, prices: List[int]) -> int:
		maxProfit = 0
		
		# Initialize two dimensional nxn array, where n is the length or prices
		# profit[i, j] = profit if bought on i and sold on j.
		profits = [[0] * len(prices) for _ in  range(0, len(prices))]
		maxP = 0
		# Profits array contains profits if a stock is bought on day i and sold on day j
		for i in range(0, len(prices)):
			for j in range(i+1, len(prices)):
				profits[i][j] = prices[j] - prices[i]
				
		# Conditions: Max transactions 2
		# Buy and sell on different days.
		# Algorithm:
		# Have a day index from day 2 to day (n-1)
		# Find max between 0 to day_index, 
		# Find max between day_index + 1 to day (n-1)
		# The sum of these two is the max profit in two transactions.
		
		for day_index in range(1, len(prices)+1):
			# max1 = max profit between day 0 to day_index
			# max2 = max profit between day day_index+1 to last day
			print("====================")
			print(f"maxProfit = {maxP}")
			print("--------------------------------------")
			print(f"day_index: {day_index}")
			max1 = 0
			max2 = 0
			for i in range(0, day_index):
				max1 = max(max1, max(profits[i][i:day_index]))
				print(f"profits: {profits[i][i:day_index]} max1 between {i} and {day_index}: {max(profits[i][i:day_index])}")
    
			for j in range(day_index, len(prices)):
				max2 = max(max2, max(profits[j][j:len(prices)]))
				print(f"profits: {profits[j][j:len(prices)]} max2 between {j} and {len(prices)}: {max(profits[j][j:len(prices)])}")
			
			maxP = max(maxP, max1 + max2)

		return maxP
    
	def maxProfit(self, prices: List[int]) -> int:
		# Initialize total profit to 0
		total_profit = 0
		
		# Loop through each day, except the last day
		for i in range(len(prices) - 1):
			# If tomorrow's price is higher than today's, buy today and sell tomorrow
			if prices[i] < prices[i + 1]:
				total_profit += prices[i + 1] - prices[i]
		
		# Return the total accumulated profit
		return total_profit


if __name__ == "__main__":
	s = Solution()
	
	# prices = [x for x in range(1, 6)]
	prices = [3,3,5,0,0,3,1,4]
	print(prices)
	
	# print(f"maxProfit >>>> {s.maxProfit3(prices)}")
	# print(f"maxProfit >>>> {s.maxP(prices)}")
	print(f"maxProfit >>>> {s.maxProfit5(prices)}")
