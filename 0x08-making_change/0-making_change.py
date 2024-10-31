#!/usr/bin/python3
"""
Module for making change using dynamic programming
Determines the fewest number of coins needed to meet a given total
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total

    Args:
        coins (list): List of coin values available
        total (int): Target total to make change for

    Returns:
        int: Fewest number of coins needed to meet total
            - Returns 0 if total is 0 or less
            - Returns -1 if total cannot be met by any combination of coins
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for optimization
    coins.sort(reverse=True)

    # Create dp array initialized with total + 1 (impossible value)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Build solution for all amounts from 1 to total
    for i in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:
                # Take minimum of current solution and solution with current coin
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
