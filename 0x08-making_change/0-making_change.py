#!/usr/bin/python3
"""
Making Change Module
This module contains a function that determines the fewest number of coins
needed to meet a given total amount using an optimized approach.
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of coin values available (integers > 0)
        total (int): Target total to make with coins

    Returns:
        int: Fewest number of coins needed to meet total
             Returns 0 if total is 0 or less
             Returns -1 if total cannot be met by any number of coins
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for a greedy approach
    coins.sort(reverse=True)

    # Memoization dictionary to store computed minimum coins for sub-totals
    memo = {}

    def backtrack(remaining):
        """
        Recursively determine the minimum number of coins needed
        for a given remaining amount, using memoization to avoid
        redundant calculations.
        
        Args:
            remaining (int): Remaining amount to make up with coins
        
        Returns:
            int: Fewest number of coins needed to meet the remaining total,
                 or -1 if it is not possible.
        """
        # If the remaining total is 0, no coins are needed
        if remaining == 0:
            return 0
        # If already computed, return the result from memo
        if remaining in memo:
            return memo[remaining]
        
        # Set minimum coins to a large number initially
        min_coins = float('inf')
        
        # Try each coin
        for coin in coins:
            if coin > remaining:
                continue  # Skip if coin is larger than the remaining total
            # Recurse with the reduced total and add one coin
            result = backtrack(remaining - coin)
            if result != -1:
                min_coins = min(min_coins, result + 1)

        # If no solution, set to -1; otherwise, set to min_coins found
        memo[remaining] = -1 if min_coins == float('inf') else min_coins
        return memo[remaining]

    # Call the backtracking function
    return backtrack(total)
