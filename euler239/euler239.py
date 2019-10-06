#! /usr/bin/env python3

import math
import itertools
import operator as op
from functools import reduce

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

    count = 0
    for p in a:
        if p:
            count = count + 1
        b.append(count)

    return b

def reduce_fraction(a, b):
    gcd = math.gcd(a,b)
    return a // gcd, b // gcd

#def choose(n, r):
#    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def cache_ncr(n, r):
    dp = [[0 for x in range(r + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, r) + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp

def choose(n, r):
    r = min(n, r)

    try:
        num = reduce(op.mul, range(n, n-r, -1))
    except TypeError:
        num = 1
    try:
        den = reduce(op.mul, range(1, r + 1))
    except TypeError:
        den = 1

    return num // den

#def num_ways(n, k, p):
#    dp = [[0 for x in range(k + 1)] for y in range(n + 1)]
#    for i in range(2, n + 1):
#        for j in range(1, k + 1):
#            if i ==
#            np = p[n]
#    return choose(np, (np-k)) * sum([(-1 if i % 2 != 0 else 1) * choose(k, i) * math.factorial(n - (np-k) - i) for i in range(k + 1)])

def solution(n, k):
    p = sieve(n)
    np = p[n]

    a = choose(np, (np-k)) * sum([(-1 if i % 2 != 0 else 1) * choose(k, i) * math.factorial(n - (np-k) - i) for i in range(k + 1)])
    #a = num_ways(n, k, p)
    a, n = reduce_fraction(a, n)
    b = math.factorial(n)

    a, b = reduce_fraction(a, b)

    print(f"{a}/{b} = {a/b}")

    # modular inverse of b, since M is prime
    b = pow(b, M - 2, M)

    # the solution
    return a * b % M

if __name__ == "__main__":
    n, k = (int(n) for n in input().split())
    #n, k = 10, 3

    print(solution(n, k))
