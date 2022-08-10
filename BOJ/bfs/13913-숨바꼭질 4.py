# and 앞에 '범위 체크'가 우선적으로 있어야 함 !!!!!!!!!!!!!!!!!

from collections import deque


def find_path(x):
    arr = []
    temp = x
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = footprint[temp]
    print(*arr[::-1])


def find_sibling(cur):
    queue = deque()
    queue.append(cur)

    while queue:
        now = queue.popleft()

        if now == k:
            print(dist[k])
            find_path(now)
            return

        for next_place in [now - 1, now + 1, now * 2]:
            if 0 <= next_place <= 100000 and not dist[next_place]:
                dist[next_place] = dist[now] + 1
                queue.append(next_place)
                footprint[next_place] = now


n, k = map(int, input().split())
dist = [0 for _ in range(100001)]
footprint = [0 for _ in range(100001)]
find_sibling(n)
