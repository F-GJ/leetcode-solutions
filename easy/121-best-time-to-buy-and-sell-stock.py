"""
Question Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=problem-list-v2&envId=array

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        min_price = prices[0]
        max_profit = 0

        print(f"Starting prices: {prices}")
        print(f"Initial minimum price: {min_price}")
        print(f"Initial maximum profit: {max_profit}")

        # enumerate() gives us both the index (day) and price
        for i, price in enumerate(prices):
            print("\n" + "=" * 45)
            print(f"ITERATION {i + 1} | DAY {i}")
            print("=" * 45)

            print(f"Current stock price: ${price}")

            print("\nSTEP 1: CHECK MINIMUM PRICE")
            print(f"Minimum price BEFORE: ${min_price}")
            print(f"Comparing min({min_price}, {price})")

            min_price = min(min_price, price)

            print(f"Minimum price AFTER:  ${min_price}")

            # STEP 2: Calculate potential profit if we sell today
            print("\nSTEP 2: CALCULATE PROFIT")
            print(f"Current selling price: ${price}")
            print(f"Cheapest buying price: ${min_price}")

            profit = price - min_price

            print(f"Calculation: {price} - {min_price} = {profit}")
            print(f"Potential profit today: ${profit}")

            print("\nSTEP 3: CHECK MAXIMUM PROFIT")
            print(f"Maximum profit BEFORE: ${max_profit}")
            print(f"Comparing max({max_profit}, {profit})")

            max_profit = max(max_profit, profit)

            print(f"Maximum profit AFTER:  ${max_profit}")

            print("\nITERATION SUMMARY")
            print(f"Day: {i}")
            print(f"Price: ${price}")
            print(f"Cheapest price so far: ${min_price}")
            print(f"Profit if sold today: ${profit}")
            print(f"Best profit so far: ${max_profit}")

        print("\n" + "=" * 45)
        print(f"FINAL MAXIMUM PROFIT: ${max_profit}")
        print("=" * 45)

        return max_profit


# Test
prices = [7, 1, 5, 3, 6, 4]

solution = Solution()
result = solution.maxProfit(prices)

print(f"\nReturned result: {result}")
