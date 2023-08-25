#!/usr/bin/python3
"""Making change O(n)"""


def makeChange(coins, total):
    """dynamic programming"""
    temp = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            temp += total // coin
            total = total % coin

    return temp if total == 0 else -1


if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
