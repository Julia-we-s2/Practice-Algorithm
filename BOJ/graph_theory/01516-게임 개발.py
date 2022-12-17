import sys
from collections import deque
input = sys.stdin.readline


def topology_sort():
    res = [0 for _ in range(n + 1)]
    queue = deque()

    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    while queue:
        cur = queue.popleft()
        res[cur] += cost[cur]
        for b in graph[cur]:
            in_degree[b] -= 1
            res[b] = max(res[b], res[cur])
            if in_degree[b] == 0:
                queue.append(b)

    return res


n = int(input())
graph = [[] for i in range(n + 1)]
in_degree = [0 for i in range(n + 1)]
cost = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    infos = list(map(int, input().split()))[:-1]

    cost[i] = infos[0]
    building_data = infos[1:]

    for j in building_data:
        graph[j].append(i)
        in_degree[i] += 1

ans = topology_sort()

for i in range(1, n + 1):
    print(ans[i])
