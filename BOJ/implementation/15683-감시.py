import sys
from copy import deepcopy
input = sys.stdin.readline


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


# 방향을 담을 조합
def dfs(depth, directions):
    if depth == len(cctvs):
        check(directions)
        return

    cctv_type = cctvs[depth][2]
    if cctv_type in (1, 3, 4):
        for i in range(4):
            dfs(depth + 1, directions + [i])
    elif cctv_type == 2:
        for i in range(2):
            dfs(depth + 1, directions + [i])
    else:
        dfs(depth + 1, directions + [0])


def check(directions):
    global ans
    new_arr = deepcopy(arr)
    for index, cctv in enumerate(cctvs):
        start_x, start_y, cctv_type = cctv
        ds = cctv_directions[cctv_type][directions[index]]

        for d in ds:
            x, y = start_x, start_y
            while True:
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 6:
                    new_arr[nx][ny] = '#'

                    x = nx
                    y = ny

                else:
                    break

    cnt = 0
    for i in range(n):
        for j in range(m):
            if new_arr[i][j] == 0:
                cnt += 1

    ans = min(ans, cnt)


# cctv 색깔 칠하는 함수
# 사각지대 개수 구하기

cctv_directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cctvs = []
ans = 1e9

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0 and arr[i][j] != 6:
            cctvs.append((i, j, arr[i][j]))

dfs(0, [])
print(ans)

