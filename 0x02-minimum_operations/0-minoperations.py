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
    min_operations = 0
    
    if n <= 1:
        return min_operations

    for i in range(2, n + 1):
        while n % i == 0:
            min_operations += i
            n /= i

    return min_operations

