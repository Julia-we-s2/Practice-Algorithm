n, m = map(int, input().split())
li = list(map(int, input().split()))

negative, positive = [], []

for i in li:
    if i < 0:
        negative.append(i)
    else:
        positive.append(i)
        
positive.sort(reverse=True)
negative.sort()
distance = []

for i in range(len(negative) // m):
    distance.append(abs(negative[i * m]))
if len(negative) % m > 0:
    distance.append(abs(negative[(len(negative) // m) * m]))

for i in range(len(positive) // m):
    distance.append(positive[i * m])
if len(positive) % m > 0:
    distance.append((positive[(len(positive) // m) * m]))

distance.sort()
ans = distance.pop()
ans += sum(distance) * 2
print(ans)