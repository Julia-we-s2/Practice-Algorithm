import sys
input = sys.stdin.readline

A, B = 100, 100
for _ in range(int(input())):
    a, b = map(int,input().split())
    if a > b:
        B -= a
    elif a < b:
        A -= b
print(A, B, sep="\n")

