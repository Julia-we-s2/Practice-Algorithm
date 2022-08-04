# 왜 이게 실버 2...?

n = int(input())

loss = [0] + list(map(int, input().split()))
gain = [0] + list(map(int, input().split()))

arr = [[0 for _ in range(101)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, 101):
        if j < loss[i]:
            arr[i][j] = arr[i - 1][j]
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i - 1][j - loss[i]] + gain[i])

print(arr[n][99])


