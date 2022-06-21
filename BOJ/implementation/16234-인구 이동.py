# 첨엔 bfs 외적으로 추가해야될 로직이 있어서 막막했는데, 하다보니까 진짜 재밌었다
# 나도 구현에 익숙해져서 언젠간 능숙하게 올 날이 오겠즤 ,,? 그때까지 꾸준히 열심히 해야겠다 !

# bfs + 검사하는 로직 => 두 개를 반복하면서 시뮬레이션 = 구현

# 하루에 여러 곳에서 일어나는 인구 이동을 어케 할 것인지
# 하루가 지나면 탐색을 어디부터 시작할 것인지 => (0, 0)부터
# 탐색을 언제까지 해야할 것인지 => country 가 0이 될 때 break

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    temp = []   # 국경선을 공유하는 나라의 좌표들을 넣는 리스트
    temp.append((a, b))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                    visited[nx][ny] = 1
                    temp.append((nx, ny))
                    queue.append((nx, ny))

    return temp


n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0

while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0

    for i in range(n):
        for j in range(n):

            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)

                if len(country) > 1:
                    flag = 1
                    num = sum([arr[x][y] for x, y in country]) // len(country)

                    for x, y in country:
                        arr[x][y] = num

    if flag == 0:
        break
    res += 1    # 하루가 흐름

print(res)
