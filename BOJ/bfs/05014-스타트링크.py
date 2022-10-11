# s -> g
# u: 위로 u층
# d: 아래로 d

from collections import deque


def bfs(cur_stair, cnt):
    queue = deque()
    queue.append((cur_stair, cnt))

    while queue:
        cur_stair, cnt = queue.popleft()

        if cur_stair == g:
            return cnt

        for next_stair in [cur_stair + u, cur_stair - d]:
            if 1 <= next_stair <= f and not visited[next_stair]:
                visited[next_stair] = 1
                queue.append((next_stair, cnt + 1))

    return "use the stairs"

f, s, g, u, d = map(int, input().split())

visited = [0 for _ in range(f + 1)]

print(bfs(s, 0))
