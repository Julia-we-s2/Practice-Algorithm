def check(row, col):
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            arr_a[i][j] = abs(1 - arr_a[i][j])


n, m = map(int, input().split())

arr_a = [list(map(int, input())) for _ in range(n)]
arr_b = [list(map(int, input())) for _ in range(n)]
cnt = 0

row_available = n - 3 + 1
col_available = m - 3 + 1

for i in range(0, row_available):
    for j in range(0, col_available):
        if arr_a[i][j] != arr_b[i][j]:
            check(i, j)
            cnt += 1

if arr_a != arr_b:
    print(-1)
else:
    print(cnt)
    