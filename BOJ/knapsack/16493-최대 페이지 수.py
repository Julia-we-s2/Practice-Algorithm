n, m = map(int, input().split())
info = [(0, 0)]
for i in range(m):
    info.append(list(map(int, input().split())))

arr = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        days = info[i][0]
        pages = info[i][1]
        if j < days:
            arr[i][j] = arr[i - 1][j]
        else:
            arr[i][j] = max(arr[i - 1][j - days] + pages, arr[i - 1][j])

print(arr[-1][-1])
