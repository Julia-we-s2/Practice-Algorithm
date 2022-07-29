from collections import defaultdict

n = int(input())
li = defaultdict(int)
for i in range(n):
    num = int(input())
    li[num] += 1

res = sorted(li.items(), key=lambda x: (-x[1], x[0]))
print(res[0][0])
