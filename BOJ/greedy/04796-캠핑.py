# l (5일 사용 가능) vs v % p (4일 사용 가능)
# 이 중 더 작은 값을 택해야 하는 이유는 8일 씩 2 칸 계산하고 나면 4 밖에 안 남기 때문
# 반대로 l 더 작은 값인  2 라고 가정하더라도, 길어야 연속 2일 밖에 이용할 수 없기에 더 큰 수인 4 는 의미가 없다
# 그렇기에 두 개의 값 중 최솟값을 답으로 선택해야 하는 것

tc = 1
while True:
    l, p, v = map(int, input().split())

    if l + p + v == 0:
        break

    cnt = 0
    cnt += (v // p) * l
    cnt += min(v % p, l)

    print('Case %d: %d' %(tc, cnt))
    tc += 1
