from collections import deque


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and li[nx][ny] == 0:
                li[nx][ny] = li[x][y] + 1
                queue.append((nx, ny))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

m, n = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
res = 0

for i in range(n):
    for j in range(m):
        if li[i][j] == 1:
            queue.append((i, j))

bfs()

for i in li:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res - 1)
