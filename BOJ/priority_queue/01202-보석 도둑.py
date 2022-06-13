# [가장 가벼운 가방에 가치가 큰 보석 담기 ! 가방이 다 찰 때까지 반복]

# 리스트로 되어 있는 원소도 해당 원소의 맨 앞의 값을 기준으로 힙 구조에 맞게 재배치된다
# 힙 구조에 따라 재배치된 값들 중 최소값이 0 번째 인덱스에 위치한다

# 이 문제 풀었더니 7 포인트 줬다 신난다 얏 호 > __ < !
# 아직 많은 문제를 풀어보지 않은 나로서 이 풀이 방식 너무 신기하다 wow

import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewelrys = []
for _ in range(n):
    heapq.heappush(jewelrys, list(map(int, input().split())))

bags = sorted([int(input()) for _ in range(k)])

temp = []
res = 0

for bag in bags:
    while jewelrys and bag >= jewelrys[0][0]:
        heapq.heappush(temp, - jewelrys[0][1])
        heapq.heappop(jewelrys)
    print(temp)

    if temp:
        res += - heapq.heappop(temp)
    elif not jewelrys:
        break

print(res)