#!/usr/bin/python3
"""
Prime Game Module
This module contains the implementation of a
prime number game between Maria and Ben
where players take turns choosing prime numbers and removing their multiples.
"""


def is_prime(n):
    """
    Check if a number is prime.
    Args:
        n (int): Number to check
    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primes_up_to(n):
    """
    Get all prime numbers up to n using Sieve of Eratosthenes.
    Args:
        n (int): Upper limit
    Returns:
        list: List of prime numbers up to n
    """
    if n < 2:
        return []

    # Initialize sieve
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    # Mark non-prime numbers
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    # Collect prime numbers
    return [i for i in range(2, n + 1) if sieve[i]]


def play_round(n):
    """
    Simulate a single round of the game.
    Args:
        n (int): Upper limit for the round
    Returns:
        str: Winner of the round ('Maria' or 'Ben')
    """
    if n < 2:
        return 'Ben'

    primes = get_primes_up_to(n)
    if not primes:
        return 'Ben'

    # If there are odd number of moves possible, Maria wins
    # (since she goes first and both play optimally)
    return 'Maria' if len(primes) % 2 == 1 else 'Ben'


def isWinner(x, nums):
    """
    Determine the winner of the prime game over multiple rounds.
    Args:
        x (int): Number of rounds
        nums (list): Array of n for each round
    Returns:
        str: Name of the winner (Maria or Ben) or None if it's a tie
    """
    if not nums or x < 1:
        return None

    if x != len(nums):
        return None

    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        winner = play_round(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
