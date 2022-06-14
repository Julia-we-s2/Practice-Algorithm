t = int(input())

for tc in range(t):
    n, k = map(int, input().split())
    li = list(map(int, input().split()))

    res = 0

    for i in li:
        res += i // k

    print(res)