n = int(input())
li = list(map(int, input().split()))
cnt = 0

li.sort()

for i in range(n):
    temp = li[:i] + li[i+1:]
    left, right = 0, len(temp) - 1

    while left < right:
        total = temp[left] + temp[right]

        if total == li[i]:
            cnt += 1
            break
        elif total > li[i]:
            right -= 1
        else:
            left += 1

print(cnt)
