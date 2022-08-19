import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    global final_sheep, final_wolf
    sheep, wolf = 0, 0

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        if arr[x][y] == 'v':
            wolf += 1
        elif arr[x][y] == 'o':
            sheep += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if arr[nx][ny] == '#':
                    continue
                visited[nx][ny] = 1
                queue.append((nx, ny))

    if wolf < sheep:
        final_sheep += sheep
    else:
        final_wolf += wolf


r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]

final_sheep = 0
final_wolf = 0

for i in range(r):
    for j in range(c):
        if not visited[i][j] and (arr[i][j] == 'v' or arr[i][j] == 'o'):
            bfs(i, j)

print(final_sheep, final_wolf)
