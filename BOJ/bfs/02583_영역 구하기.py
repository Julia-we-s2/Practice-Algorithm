from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

areas = []


def bfs(s1, s2):
    queue = deque()
    queue.append((s1, s2))
    arr[s1][s2] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1

    areas.append(cnt)


m, n, k = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(m)]

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for j in range(x1, x2):
        for l in range(y1, y2):
            arr[l][j] = 1

for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            bfs(i, j)

print(len(areas))
areas.sort()
for i in areas:
    print(i, end=' ')