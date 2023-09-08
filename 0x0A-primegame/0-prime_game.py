#!/usr/bin/python3
"""
Maria and Ben are playing game,
Given a set of consecutive integers starting from 1,
Return: name of the player that won most rounds,
If winner not determined, return None,
Assume n and x will not be larger than 10000,
"""


def isWinner(x, nums):
    """ x is num of rounds
    nums is an array of n
    """
    def is_prime(num):
        """ check if num is a prime num
        """
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
            return True

    def win(n):
        """ determine winner
        """
        if n <= 1:
            return False
        if n in rounds:
            return rounds[n]

        for i in range(2, n + 1):
            if is_prime(i):
                if not win(n - 1):
                    rounds[n] = True
                    return True
        rounds[n] = False
        return False

    winner = []

    for n in nums:
        rounds = {}
        if win(n):
            winner.append("Maria")
        else:
            winner.append("Ben")

    maria_wins = winner.count("Maria")
    ben_wins = winner.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
