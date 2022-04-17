def bfs():
    res = 1
    queue = set([(0, 0, li[0][0])])

    while queue:
        x, y, alphabet = queue.pop()
        res = max(res, len(alphabet))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and li[nx][ny] not in alphabet:
                queue.add((nx, ny, alphabet + li[nx][ny]))

    return res

dx = [0, 0, 1, -1]
dy = [1,-1, 0, 0]

r, c = map(int, input().split())
li = [list(map(str, input().strip())) for _ in range(r)]

print(bfs())