dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(cur_x, cur_y, dist):
    global cnt
    visited[cur_x][cur_y] = 1

    if cur_x == 0 and cur_y == c - 1:
        if dist == k:
            cnt += 1
        return

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if not visited[nx][ny] and arr[nx][ny] != 'T':
                visited[nx][ny] = 1
                dfs(nx, ny, dist + 1)
                visited[nx][ny] = 0


r, c, k = map(int, input().split())
arr = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
cnt = 0
dfs(r - 1, 0, 1)
print(cnt)
