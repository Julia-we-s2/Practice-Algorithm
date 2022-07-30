import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))
min_value = sys.maxsize
ans = [0, 0, 0]

for i in range(n - 2):
    left = i + 1
    right = n - 1
    while left < right:
        total = nums[i] + nums[left] + nums[right]

        if abs(total) < min_value:
            min_value = abs(total)
            ans = [nums[i], nums[left], nums[right]]

        if total < 0:
            left += 1
        elif total > 0:
            right -= 1
        else:
            break

print(*ans)
