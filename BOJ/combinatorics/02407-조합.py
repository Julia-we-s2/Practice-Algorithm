import sys


def fac(k):
    num = 1
    for i in range(2, k + 1):
        num *= i
    return num


n, m = map(int, sys.stdin.readline().split())
print(fac(n) // (fac(n - m) * fac(m)))