#! /usr/bin/env python3

import math
import itertools

M = 10**9 + 123

def square(n):
    return n * n

def sieve(n):
    a = [True for i in range(n + 1)]

    candidates = range(2, math.ceil(math.sqrt(n)))

    a[0] = False
    a[1] = False

    for i in candidates:
        if a[i]:
            for j in range(i * 2, n + 1, i):
                a[j] = False

    b = []

    for i,p in enumerate(a):
        if p:
            b.append(i)

    return b

def reduce(a, b):
    gcd = math.gcd(a,b)
    return a // gcd, b // gcd

def choose(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def derangements(n):
    dp = [0 for x in range(n + 1)]

    dp[0] = 1
    dp[1] = 0
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2])

    return dp[n]

def subfact(n):
    if n in [2, 0]:
        return 1
    elif n in [1]:
        return 0
    elif 1 <= n <= 18:
        return round(math.factorial(n) / math.e)
    elif n.imag == 0 and n.real == int(n.real) and n > 0:
        return (n - 1) * (subfact(n - 1) + subfact(n - 2))
    else:
        raise ValueError

if __name__ == "__main__":
    #n, k = (int(n) for n in input().split())
    n, k = 10, 3

    P = len(sieve(n))

    # we need to find a and b
    """
    a -> number of ways to get condition
    b -> n!

    then reduce a/b to get final a and b
    """

    b = math.factorial(n)
    n = n - P + k

    s = 0
    for i in range(n-k+1):
        s += choose(n-k, i) * derangements(n - i)

    a = choose(P, k) * s

    a, b = reduce(a, b)

    b = pow(b, M - 2, M)

    # print the solution
    print(a * b % M)