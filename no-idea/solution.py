#! /usr/bin/env python3

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    a = set(map(int, input().strip().split()))
    b = set(map(int, input().strip().split()))

    happiness = sum([1 if v in a else -1 if v in b else 0 for v in arr])
    print(happiness)
