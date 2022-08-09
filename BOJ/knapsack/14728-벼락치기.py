n, t = map(int, input().split())
study = [(0, 0)]

for _ in range(n):
    k, s = map(int, input().split())
    study.append((k, s))

arr = [[0 for _ in range(t + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, t + 1):
        time = study[i][0]
        score = study[i][1]

        if j < time:
            arr[i][j] = arr[i - 1][j]
        else:
            arr[i][j] = max(arr[i - 1][j - time] + score, arr[i - 1][j])

print(arr[i][j])
