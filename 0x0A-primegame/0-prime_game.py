#!/usr/bin/python3
"""
Maria and Ben are playing game,
Given a set of consecutive integers starting from 1,
Return: name of the player that won most rounds,
If winner not determined, return None,
Assume n and x will not be larger than 10000,
"""


def check_prime(n):
    """ Check if n is a prime number """
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def add_prime(n, prime_num):
    """ Add prime number to list """
    last_prime = prime_num[-1]
    if n > last_prime:
        for i in range(last_prime + 1, n + 1):
            if check_prime(i):
                prime_num.append(i)
            else:
                prime_num.append(0)


def isWinner(x, nums):
    """ x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    """

    score = {"Maria": 0, "Ben": 0}
    prime_num = [0, 0, 2]
    add_prime(max(nums), prime_num)

    for round in range(x):
        new_sum = sum((i != 0 and i <= nums[round])
                    for i in prime_num[:nums[round] + 1])
        if (new_sum % 2):
            winner = "Maria"
        else:
            winner = "Ben"
        if winner:
            score[winner] += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Ben"] > score["Maria"]:
        return "Ben"

    return None
