import sys
input = sys.stdin.readline
t = int(input())

for tc in range(t):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]

    ordered_li = sorted(li, key=lambda x: x[0])

    person = ordered_li[0][1]
    cnt = 1

    for i in range(1, n):
        if ordered_li[i][1] < person:
            person = ordered_li[i][1]
            cnt += 1

    print(cnt)
