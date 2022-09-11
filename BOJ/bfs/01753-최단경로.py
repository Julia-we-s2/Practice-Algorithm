import heapq

v, e = map(int, input().split())
k = int(input())
INF = int(1e9)

graph = [[] * (v+1) for _ in range(v+1)]
distance = [INF] * (v+1)

for i in range(e):
  u, v, w = map(int, input().split())
  # u -> v 의 비용 w
  graph[u].append((v, w))
  
def dijkstra(start):
  heap = []
  heapq.heappush(heap, (0, start))
  distance[start] = 0

  while heap:
    dist, now = heapq.heappop(heap)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(heap, (cost, i[0]))

dijkstra(k)

for i in range(1, v+1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])
