import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append(home)
    while queue:
        x, y = queue.popleft()
        if abs(x - festival[0]) + abs(y - festival[1]) <= 1000:
            print("happy")
            return

        for i in range(n):
            if not visited[i]:
                nx, ny = conv[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    queue.append([nx,ny])
                    visited[i] = 1
    print("sad")
    return


t = int(input())

for tc in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    conv = []
    for i in range(n):
        conv.append(list(map(int, input().split())))
    festival = list(map(int, input().split()))
    visited = [0 for i in range(n+1)]
    bfs()