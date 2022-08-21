n = int(input())
li = [int(input()) for _ in range(n)]
cnt = 1
stick = li[-1]

for i in range(n - 1, -1, -1):
    if li[i - 1] > stick:
        stick = li[i - 1]
        cnt += 1
print(cnt)
