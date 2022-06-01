import heapq
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
li = []

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append((1, v))

min_heap = [(0, x)]
visited = set()
distance = {i: float('inf') for i in range(1, n + 1)}
distance[x] = 0

while min_heap:
    cur_distance, u = heapq.heappop(min_heap)
    if u in visited:
        continue

    visited.add(u)

    if len(visited) == n:
        break

    for direct_distance, v in graph[u]:

        if cur_distance + direct_distance < distance[v] and v not in visited:
            distance[v] = cur_distance + direct_distance
            heapq.heappush(min_heap, (cur_distance + direct_distance, v))

for i in range(1, n + 1):
    if distance[i] == k:
        li.append(i)

if li:
    print(*li)
else:
    print(-1)