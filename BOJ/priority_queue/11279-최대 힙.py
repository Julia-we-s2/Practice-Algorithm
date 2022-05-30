import sys
import heapq
input = sys.stdin.readline

h = []
n = int(input())

for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(h, -x)
    else:
        print(-1 * heapq.heappop(h)) if h else print(0)