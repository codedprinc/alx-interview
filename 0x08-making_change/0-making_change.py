#!/usr/bin/python3
"""
Making Change Module
This module contains a function that determines the fewest number of coins
needed to meet a given total amount.
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

    # Sort coins in descending order for optimization
    coins = sorted(coins, reverse=True)

    # Initialize dp array with total + 1 (impossible value)
    # as we can't use more coins than the total itself
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Build solution for all amounts from 1 to total
    for i in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:
                # If using this coin gives better solution, update dp[i]
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, no solution exists
    return dp[total] if dp[total] != float('inf') else -1
