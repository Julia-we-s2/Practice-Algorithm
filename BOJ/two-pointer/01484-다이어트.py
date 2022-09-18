g = int(input())
current = [x for x in range(1, 100001)]
remembered = [x for x in range(1, 100001)]
n, m = 100000, 100000
left, right = 0, 0
res = []

while left < n and right < m:
    temp = (current[left] + remembered[right]) * (current[left] - remembered[right])
    if temp == g:
        res.append(current[left])
    if temp < g:
        left += 1
    else:
        right += 1

if not res:
    print(-1)
else:
    for i in res:
        print(i)