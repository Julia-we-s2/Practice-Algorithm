# 아직까지도 머릿속으로 잘 안 그려진다
# 좀만 변형해도 적용을 못 해버리니 ^_^ 이분 탐색 연습이 좀 더 필요하다...! 

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
li = sorted(list(int(input()) for _ in range(n)))

end = li[-1] - li[0]
start = 1
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    cur = li[0]

    for i in range(1, len(li)):
        if li[i] >= cur + mid:
            cnt += 1
            cur = li[i]

    if cnt >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
