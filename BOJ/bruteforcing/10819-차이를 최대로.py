from itertools import permutations

n = int(input())
a = list(map(int, input().split()))

per = permutations(a)
ans = 0

for i in per:
    total = 0
    for j in range(len(i) - 1):
        total += abs(i[j] - i[j + 1])
        
    if total > ans:
        ans = total
        
print(ans)