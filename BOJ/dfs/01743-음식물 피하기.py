import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    global largest
    cnt = 1
    visited[x][y] = 1
    st = [(x, y)]

    while st:
        x, y = st.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    cnt += 1
                    st.append((nx, ny))

    if cnt > largest:
        largest = cnt


n, m, k = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0] * m for _ in range(n)]
largest = - 1

for _ in range(k):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            dfs((i, j))

print(largest)