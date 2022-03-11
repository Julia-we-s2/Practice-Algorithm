from collections import deque

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]


def bfs():
    global cnt

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if li[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

    cnt += 1


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    li = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    queue = deque()
    cnt = 0

    for i in range(h):
        for j in range(w):
            if li[i][j] == 1 and visited[i][j] == 0:
                queue.append((i, j))
                visited[i][j] = 1
                bfs()

    print(cnt)

