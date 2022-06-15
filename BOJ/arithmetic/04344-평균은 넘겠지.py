c = int(input())

for tc in range(c):
    li = list(map(int, input().split()))
    n = li[0]
    scores = li[1:]
    avg = sum(li[1:]) // n
    cnt = 0

    for i in scores:
        if i > avg:
            cnt += 1
    rate = (cnt / n) * 100
    print('{0:0.3f}%'.format(rate))

