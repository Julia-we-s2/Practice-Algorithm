from itertools import permutations
from collections import deque


def bfs(start, finish, cnt_p):
    global distance

    queue = deque()
    queue.append(start, distance)

    while queue:
        x_and_y, distance = queue.popleft()
        x, y = x_and_y
        visited[x][y] = 1
     
        if (x, y) == finish:
            print('끝나ㅕ',x ,y, distance)
            start = (x, y)

            for i in range(n):
                for j in range(n):
                    if li[i][j] == -li[x][y]:
                        print((x,y), (i, j), distance)
                        bfs((x,y), (i,j), distance)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                queue.append(((nx, ny), cnt + 1))
                visited[nx][ny] = 1
                print(queue)

        for row in visited:
            print(*row)


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input())
for tc in range(t):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    monster = []

    for i in range(n):
        for j in range(n):
            if li[i][j] != 0 and li[i][j] > 0:
                monster.append((i, j))

    for p in permutations(monster, len(monster)):
        print('몬스터', p)
        cnt = 0
        distance = 0
        visited = [[0] * n for _ in range(n)]
        for each in p:
            print('each', each)
            bfs((0, 0), each, 0)


