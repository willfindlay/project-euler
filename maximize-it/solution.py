#! /usr/bin/env python3

import os, sys
from functools import reduce
import itertools

def f(x):
    return x * x

def s(ell, m):
    return sum(map(f, ell)) % m

def maximize(possibilities, m):
    return max([s(poss, m) for poss in possibilities])

if __name__ == "__main__":
    k, m = map(int, input().split(' '))

    lists = []
    for i in range(k):
        lists.append(list(map(int, input().split(' ')))[1:])

    possibilities = itertools.product(*lists)

    print(maximize(possibilities, m))
