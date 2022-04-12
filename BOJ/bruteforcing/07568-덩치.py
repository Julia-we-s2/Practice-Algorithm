n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
check = []

for i in range(n):
    cnt = 0
    for j in range(n):
        if li[i][0] < li[j][0] and li[i][1]< li[j][1]:
            cnt += 1
    check.append(cnt + 1)

for k in check:
    print(k, end=" ")
