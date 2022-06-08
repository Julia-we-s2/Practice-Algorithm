n = int(input())
m = int(input())
broken = set(input().split())

ans = abs(100 - n)

for num in range(1000001):
    for i in str(num):
        if i in broken:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - n))

print(ans)
