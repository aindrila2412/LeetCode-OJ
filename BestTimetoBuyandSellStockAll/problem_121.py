#!/usr/bin/python

"""
approach 1: O(n2)
approach 2: O(n)
"""

class Solution(object):
    def max_profit_brute_force(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for outer in range(len(prices)):
            for inner in range(len(prices)):

                # get indices
                before = min(outer, inner)
                after = max(outer, inner)

                # values at those indices
                before_price = prices[before]
                after_price = prices[after]

                # potential profit
                could_be_profit = after_price - before_price

                # max so far calculation
                max_profit = max(max_profit, could_be_profit)

        return max_profit

    def max_profit_efficient(self, prices):

        max_profit, min_price = 0, float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
            profit_ledger.append(max_profit)

    def max_profit_total(self, prices):

        total_profit = 0

        for i in range (0, len(prices)-1):
            if prices[i+1] > prices [i]:
                total_profit += prices[i+1] - prices[i]
        return total_profit

if __name__ == "__main__":
    prices = [7,6,4,3,1]
    sol = Solution()
    print sol.max_profit_total(prices)
