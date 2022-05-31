import heapq

h = []
n = int(input())

for _ in range(n):
    value = input()

    if value == '0':
        print(-heapq.heappop(h) if h else -1)
    else:
        li = list(map(int, value.split()))
        for i in li[1:]:
            heapq.heappush(h, -i)