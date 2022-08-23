import sys, heapq
from collections import defaultdict
input = sys.stdin.readline


def dijkstra(start, end):
    dist = [1e9 for _ in range(n + 1)]
    path = [-1 for _ in range(n + 1)]
    dist[start] = 0

    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)
        if dist[cur_node] < cur_dist:
            continue
        for distance, next_node in graph[cur_node]:
            cost = cur_dist + distance
            if cost < dist[next_node]:
                dist[next_node] = cost
                path[next_node] = cur_node
                heapq.heappush(queue, (cost, next_node))

    return dist[end], path


n = int(input())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

s, e = map(int, input().split())
min_cost, path_li = dijkstra(s, e)

temp = e
res_path = [e]

while path_li[temp] != -1:
    res_path.append(path_li[temp])
    temp = path_li[temp]

print(min_cost)
print(len(res_path))
for i in res_path[::-1]:
    print(i, end=' ')
