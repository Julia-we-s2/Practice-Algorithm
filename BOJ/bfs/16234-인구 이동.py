from collections import deque


def bfs(x, y):
    global cnt

    queue = deque()
    queue.append((x, y))
    move_queue = deque()
    population, size = 0, 0

    while queue:
        x, y = queue.popleft()
        move_queue.append((x, y))
        population += li[x][y]
        size += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if l <= abs(li[nx][ny] - li[x][y]) <= r and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

    cnt += 1

    while move_queue:
        x, y = move_queue.popleft()
        li[x][y] = population // size

    print(li)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, l, r = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i, j)

print(cnt)