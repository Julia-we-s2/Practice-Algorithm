d, n = map(int, input().split())
oven_depths = list(map(int, input().split()))
doughs_done = list(map(int, input().split()))

for i in range(d - 1):
    if oven_depths[i] < oven_depths[i + 1]:
        oven_depths[i + 1] = oven_depths[i]

cur = 0

for i in range(d - 1, -1, -1):
    if doughs_done[cur] > oven_depths[i]:
        continue

    cur += 1
    if cur >= n:
        print(i + 1)
        exit(0)

print(0)
