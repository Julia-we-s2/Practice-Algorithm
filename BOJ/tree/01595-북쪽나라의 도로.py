# 어쨌든 다익스트라로는 시간 초과 때문에 안 풀리는 문제 
# 좀 더 분발해야한다!! 

# 결국은 트리의 지름 구하는 문제였다는 거! 
# bfs 2번
 
# visited 인덱스를 도시의 개수 + 1까지 설정해야 채점 100%에서 indexError가 안 난다,,, ㄴㅇㄱ

import sys
from collections import deque, defaultdict
input = sys.stdin.readline


def bfs(start):
    global max_dist
    visited = [-1 for _ in range(10001)]
    queue = deque()
    queue.append(start)
    visited[start] = 0

    while queue:
        cur_node = queue.popleft()

        for next_node, cost in graph[cur_node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[cur_node] + cost
                queue.append(next_node)

    max_value = (max(visited), visited.index(max(visited)))
    return max_value


graph = defaultdict(list)
flag = 1
max_dist = -1

while flag:
    try:
        a, b, cost = map(int, input().split())
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    except:
        flag = 0
        break

max_dist, node = bfs(1)
max_dist, node = bfs(node)

print(max_dist)
