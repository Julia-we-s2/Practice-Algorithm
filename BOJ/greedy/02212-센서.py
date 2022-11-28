n = int(input())
k = int(input())
locations = sorted(list(map(int, input().split())))

if k >= n:
    print(0)
    exit(0)

dist = []
for i in range(1, n):
    dist.append(locations[i] - locations[i - 1])

dist.sort(reverse=True)

for _ in range(k - 1):
    dist.pop(0)

print(sum(dist))
