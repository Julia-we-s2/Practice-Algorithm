from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    queue = deque([start])
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    cnt = 1

    while queue:
        s = queue.popleft()

        for i in li[s]:
            if not visited[i]:
                visited[i] = 1
                cnt += 1
                queue.append(i)
    return cnt


n, m = map(int, input().split())
li = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    li[b].append(a)

res = []
max_cnt = 0

for i in range(1, n+1):
    tmp = bfs(i)
    if max_cnt == tmp:
        res.append(i)
    if max_cnt < tmp:
        max_cnt = tmp
        res.clear()
        res.append(i)

print(*res)