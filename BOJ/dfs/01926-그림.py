dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(argument):
    global cnt, max_scale
    scale = 1

    x, y = argument
    st = []
    st.append((x, y))
    visited[x][y] = 1

    while len(st):
        cur = st[-1]
        st.pop()
        x, y = cur

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    scale += 1
                    visited[nx][ny] = 1
                    st.append((nx, ny))

    max_scale = max(max_scale, scale)
    cnt += 1


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

cnt = 0
max_scale = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            dfs((i, j))

print(cnt)
print(max_scale)