from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, height, visited):
    global cnt
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] >= height and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
safe_area = []

min_height = min(map(min, arr))
max_height = max(map(max, arr))

for height in range(min_height - 1, max_height + 1):
    cnt = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for k in range(n):
            if arr[j][k] >= height and visited[j][k] == 0:
                cnt += 1
                bfs(j, k, height, visited)

    safe_area.append(cnt)

print(max(safe_area))


