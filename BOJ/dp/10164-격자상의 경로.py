# 눈물 날 것 같다 내가 dp 를 처리했다

# k 가 0일 때랑 아닐 때를 구분
# k 가 0이 아닌 경우에는, (1, 1) 부터 k 지금까지 경우의 수 * k 부터 (n, m)까지의 경우의 수

import sys
input = sys.stdin.readline


def search(n, m):
    dp = [[0] * (m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = 1
                continue
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n][m]


n, m, k = map(int, input().split())

if k == 0:
    print(search(n, m))
else:
    x, y = 0, 0
    for i in range(1, 16):
        if m * i - (m - 1) <= k < m * (i + 1) - (m - 1):
            x = i
            y = k - (m * i - (m - 1)) + 1
            break

    x2 = n - x + 1
    y2 = m - y + 1

    print(search(x, y) * search(x2, y2))
