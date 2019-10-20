#! /usr/bin/env python3

def soln(a, d, n, x):
    def u(k):
        return (a - d * k) * (r ** (k - 1))

    def s(n):
        return sum([u(k) for k in range (1, n + 1)])
