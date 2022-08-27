from collections import deque


def bfs(start, end):
    queue = deque()
    queue.append((start, 0))

    visited = [0 for _ in range(n + 1)]
    visited[start] = 1

    while queue:
        cur_node, cur_dist = queue.popleft()

        if cur_node == end:
            return cur_dist

        for next_node, next_dist in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = 1
                queue.append((next_node, cur_dist + next_dist))


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

for _ in range(m):
    a, b = map(int, input().split())
    print(bfs(a,b))
