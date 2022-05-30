import sys
import heapq
input = sys.stdin.readline

h = []
n = int(input())

for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(h, x)

    else:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)