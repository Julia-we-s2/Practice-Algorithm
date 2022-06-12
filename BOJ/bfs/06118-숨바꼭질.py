from collections import deque


def bfs(start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
maximum = max(visited)
print(visited.index(maximum), maximum - 1, visited.count(maximum))
