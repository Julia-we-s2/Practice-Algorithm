# dp[0] = 0, dp[1] = 1 을 미리 선언하고 가면 IndexError 발생한다
# 0 인 경우, dp = [0 for _ in range(n + 1)] 이면 1번째 인덱스가 안 만들어지기 때문
# 그래서 (n + 2) 로 범위를 설정하면 맞게 되긴 한다


# 풀이 1 : dp

n = int(input())
dp = [0 for _ in range(n + 1)]

for i in range(0, n + 1):
    if i == 0:
        dp[0] = 0
    elif i == 1:
        dp[1] = 1
    else:
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])


# 풀이 2: append

n = int(input())
fibo = [0, 1]

for i in range(2, n + 1):
    fibo.append(fibo[i - 1] + fibo[i - 2])

print(fibo[n])


# 풀이 3: 현재 값과 이전 값 더하기

def fibo(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x
print(fibo(int(input())))