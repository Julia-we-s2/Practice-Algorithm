from collections import deque
import sys
input = sys.stdin.readline


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    while queue:
        x, y = queue.popleft()
        if visited[x][y] != 'FIRE':
            flag = visited[x][y]
        else:
            flag = 'FIRE'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < height and 0 <= ny < width:
                if visited[nx][ny] == -1 and (
                    arr[nx][ny] == '.' or arr[nx][ny] == '@'
                ):
                    if flag == 'FIRE':
                        visited[nx][ny] = flag
                    else:
                        visited[nx][ny] = flag + 1
                    queue.append((nx, ny))
            else:
                if flag != 'FIRE':
                    return flag + 1

    return 'IMPOSSIBLE'


t = int(input())
for tc in range(t):
    width, height = map(int, input().split())
    arr = [list(input()) for _ in range(height)]
    visited = [[-1 for _ in range(width)] for _ in range(height)]
    queue = deque()
    for i in range(height):
        for j in range(width):
            if arr[i][j] == '*':
                visited[i][j] = 'FIRE'
                queue.append((i, j))
            elif arr[i][j] == '@':
                visited[i][j] = 0
                start = (i, j)

    queue.append(start)
    print(bfs())
