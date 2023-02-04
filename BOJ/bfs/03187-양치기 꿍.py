from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    sheep, wolf = 0, 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        if arr[x][y] == 'v':
            wolf += 1
        elif arr[x][y] == 'k':
            sheep += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if not visited[nx][ny] and arr[nx][ny] != '#':
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

    return sheep, wolf


def check_nums(sheep, wolf):
    global total_sheep, total_wolf

    if sheep > wolf:
        total_sheep += sheep
    else:
        total_wolf += wolf


row, col = map(int, input().split())
total_sheep, total_wolf = 0, 0
arr = []
for _ in range(row):
    arr.append(list(input()))

visited = [[0 for _ in range(col)] for _ in range(row)]

for i in range(row):
    for j in range(col):
        if not visited[i][j] and (arr[i][j] == 'v' or arr[i][j] == 'k'):
            s, w = bfs(i, j)
            check_nums(s, w)

print(total_sheep, total_wolf)
