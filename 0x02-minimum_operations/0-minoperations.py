#!/usr/bin/python3
"""
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that calculates
the fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Returns an integer
    if n is impossible achieve
    else returns 0
    """
    if n == 1:
        return 0

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = float('inf')
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))

    return dp[n] if dp[n] != float('inf') else 0
