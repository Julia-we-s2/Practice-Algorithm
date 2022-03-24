n = int(input())

li = list(map(int, input().split()))
x = int(input())

cnt = 0
li.sort()

left, right = 0, n-1

while left < right:
    total = li[left] + li[right]
    if total == x:
        cnt += 1
        left += 1
    elif total > x:
        right -= 1
    else:
        left += 1

print(cnt)