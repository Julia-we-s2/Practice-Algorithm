from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [0, 0, 1, -1, 0, 0]


def bfs(x, y, z):
    q.append([x, y, z])
    visited[x][y][z] = 1

    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                if s[nx][ny][nz] == 'E':
                    print("Escaped in {0} minute(s).".format(visited[x][y][z]))
                    return
                if s[nx][ny][nz] == '.' and visited[nx][ny][nz] == 0:
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    q. append([nx, ny, nz])
    print("Trapped!")


while True:
    l, r, c = map(int, input().split())
    # // l 층 수, r 행, c 열

    if l == 0 and r == 0 and c == 0:
        break

    s = [[[] * c for _ in range(r)] for _ in range(l)]
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]

    q = deque()

    for i in range(l):
        s[i] = [list(map(str, input().strip())) for _ in range(r)]
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if s[i][j][k] == 'S':
                    bfs(i, j, k)
