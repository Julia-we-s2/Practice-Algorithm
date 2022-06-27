import sys
input = sys.stdin.readline


def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1

    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if matrix[nx][ny] < matrix[x][y]:
                visited[x][y] += dfs(nx, ny)
    return visited[x][y]


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1 for _ in range(n)] for _ in range(m)]
print(dfs(0, 0))
