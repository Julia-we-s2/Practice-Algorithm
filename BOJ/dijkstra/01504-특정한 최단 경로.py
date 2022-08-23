import sys, heapq
from collections import defaultdict
input = sys.stdin.readline


def dijkstra(start, end):
    dist = [1e9 for _ in range(n + 1)]
    dist[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)

        for distance, next_node in graph[cur_node]:
            cost = cur_dist + distance
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(queue, (cost, next_node))

    return dist[end]


n, e = map(int, input().split())
graph = defaultdict(list)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

stop1, stop2 = map(int, input().split())

path1 = dijkstra(1, stop1) + dijkstra(stop1, stop2) + dijkstra(stop2, n)
path2 = dijkstra(1, stop2) + dijkstra(stop2, stop1) + dijkstra(stop1, n)
res = min(path1, path2)

print(-1 if res >= 1e9 else res)
