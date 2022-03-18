n, k = map(int, input().split())

li = [i for i in range(1, (n+1))]
ans = []
num = k - 1

for i in range(n):
    if len(li) > num:
        ans.append(li.pop(num))
        num += k - 1
    elif len(li) <= num:
        num %= len(li)
        ans.append(li.pop(num))
        num += k - 1

print('<', ', '.join(str(i) for i in ans), '>', sep='')
