# 사탕 묶음의 개수인지 사탕 낱개의 개수인지 헷갈리자 말자 ! ^_^;

import sys
input = sys.stdin.readline


def check(data):
    maximum = 1

    for i in range(n):
        cnt = 1
        for j in range(n - 1):
            if data[i][j] == data[i][j + 1]:
                cnt += 1
            else:
                cnt = 1
            maximum = max(maximum, cnt)

        cnt = 1
        for j in range(n - 1):
            if data[j][i] == data[j + 1][i]:
                cnt += 1
            else:
                cnt = 1
            maximum = max(maximum, cnt)

    return maximum


n = int(input())
arr = [list(input()) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n - 1):

        if arr[i][j] != arr[i][j + 1]:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            temp = check(arr)
            ans = max(ans, temp)
            arr[i][j + 1], arr[i][j] = arr[i][j], arr[i][j + 1]

        if arr[j][i] != arr[j + 1][i]:
            arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
            temp = check(arr)
            ans = max(ans, temp)
            arr[j + 1][i],  arr[j][i] = arr[j][i], arr[j + 1][i]

print(ans)

