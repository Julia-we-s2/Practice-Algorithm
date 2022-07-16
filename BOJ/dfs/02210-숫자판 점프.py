import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, num):
    global cnt

    if len(num) == 6:
        if num not in ans:
            ans.add(num)
            cnt += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num + arr[nx][ny])


arr = [list(input().split()) for _ in range(5)]
cnt = 0
ans = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])

print(cnt)
