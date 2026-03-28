from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Thoughts
        --------
        Naive thoughts:
        We can sum all possible combinations in nested loop and return the max
        If I am not wrong, it will be O(n^2) time complexity

        Pseudocode
        -----------
        max_profit = 0
        n = len(prices)
        for i in range(n-1):
            for j in range(i+1, n):
                profit = prices[i] + prices[j]
                if profit > max_profit:
                    max_profit = profit
        return profit

        Complexity
        ----------
        Time Complexity: O(n^2) # Two nested loops, each upto n interations
        Space Complexity: O(1) # Only few scalar variables 

        LeetCode Submission Result
        --------------------------
        Time Limit Exceeded
        198 / 212 testcases passed

        """
        max_profit = 0
        n = len(prices)
        for i in range(n - 1):
            for j in range(i + 1, n):
                #print (i, j, prices[i], prices[j], end=", ")
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
                #print(profit, max_profit)
        return max_profit


    def maxProfit_v2(self, prices: List[int]) -> int:
        """
        Thoughts
        --------
        Need to solve for time complexity => There exists a solution better than O(n^2)

        In each iteration, let's try to keep note of the min_price as well on top of max_profit, and see if it helps. No need nested loop. 

        Pseudocode
        -----------
        min_price = prices[0]
        max_profit = 0 # Initially, no profit since no transaction is made
        
        for price in prices[1:]: 
            if price > min_price: # If True, technically we can get a profit by selling
                profit = price - min_price # We cannot pick this as the best profit yet
                if profit > max_profit:
                    max_profit = profit
            else
               min_price = price

        return max_profit

       

        Complexity
        ----------
        Time Complexity: O(n) - single pass through array
        Space Complexity: O(1) - Only scalar components: min_price, max_profit, profit

        LeetCode Submission Result
        --------------------------
        212 / 212 testcases passed
        Runtime 17 ms Beats 97.61%
        """

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price > min_price:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
            else:
                min_price = price
            print(min_price, price, max_profit)
        
        return max_profit

    def maxProfit_v2b(self, prices: List[int]) -> int:
        """
        Thoughts
        --------
        Same logic as above, bit with clean code
        """
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            min_price = min(price, min_price) # Always track lowest
            profit = price - min_price
            max_profit = max(profit, max_profit) # Always track highest

        return max_profit
        



# Test cases
if __name__ == "__main__":
    s = Solution()

    # Example 1: Buy day 2 (price=1), sell day 5 (price=6) → profit=5
    assert s.maxProfit_v2b([7, 1, 5, 3, 6, 4]) == 5

    # Example 2: No profit possible (descending prices)
    assert s.maxProfit_v2b([7, 6, 4, 3, 1]) == 0

    # Single element
    assert s.maxProfit_v2b([5]) == 0

    # Two elements with profit
    assert s.maxProfit_v2b([1, 2]) == 1

    # Edge case
    assert s.maxProfit_v2b([3, 2, 1, 1, 5]) == 4

    print("All tests passed!")
