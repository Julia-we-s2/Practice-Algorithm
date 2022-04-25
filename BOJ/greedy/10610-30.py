li = list(input())
li.sort(reverse=True)

total = 0

for i in li:
    total += int(i)
if total % 3 != 0 or '0' not in li:
    print(-1)
else:
    print(''.join(li))
