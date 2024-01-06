class Solution1:
    def maxProfit(self, prices: list) -> int:
        # Algo: Brute force
        max_profit = 0
        max_buy_index = 0
        max_sell_index = 0

        last = len(prices)

        # Use indices to iterate through the array
        for i in range(last):
            # Optimization 1
            try:
                if prices[i + 1] <= prices[i]:
                    continue
            except:
                pass

            for j in range(i + 1, last):
                # Optimization 2
                try:
                    if prices[j + 1] >= prices[j]:
                        continue
                except:
                    pass

                profit = prices[j] - prices[i]

                if profit > max_profit:
                    max_profit = profit
                    max_buy_index = i
                    max_sell_index = j

        return max_profit


class Solution2:
    def maxProfit(self, prices: list) -> int:
        # print("++++")
        # print(prices)
        # Algo: Brute force
        max_profit = 0
        last = len(prices)

        if last <= 1:
            return 0

        min_price = min(prices)
        min_price_first_occurence_index = prices.index(min_price)

        max_price = max(prices)

        # Search for last occurence of the max price
        max_price_last_occurence_index = 0
        for index in range(last - 1, -1, -1):
            if prices[index] == max_price:
                max_price_last_occurence_index = index
                break

        # If max price occurs after min price, we got the max profit. Return
        if max_price_last_occurence_index > min_price_first_occurence_index:
            max_profit = max_price - min_price
            return max_profit

        # Otherwise, recursively call maxProfit with 3 Sub lists.
        # a) 0 to max_price index.
        # b) max_price_index + 1 to min_price_index -1
        # c) min_price_index to last.

        try:
            p1 = self.maxProfit(prices[0 : max_price_last_occurence_index + 1])
        except:
            p1 = 0

        try:
            p2 = self.maxProfit(
                prices[
                    max_price_last_occurence_index + 1 : min_price_first_occurence_index
                ]
            )
        except:
            p2 = 0

        try:
            p3 = self.maxProfit(prices[min_price_first_occurence_index:])
        except:
            p3 = 0

        return max(p1, p2, p3)


class Solution:
    def maxProfit(self, prices: list) -> int:
        if not prices:
            return 0

        # Assume the first price is the minimum
        min_price = prices[0] 
        max_profit = 0

        for price in prices:
            # Update the min_price is a lower price is found. This represents the buying price.
            min_price = min(min_price, price)

            # Calculate the profit as if we are selling today at price, after buying at min_price.
            # This ensures we are always selling after a potential buy.
            profit = price - min_price

            # Update the max_profit is the calculated profit is higher than the current max_profit.
            max_profit = max(max_profit, profit)

        return max_profit


def main():
    s = Solution()
    prices = [6, 10, 1, 2]

    max_profit = s.maxProfit(prices)
    print(max_profit)


main()
