n = int(input())
nums = set(list(map(int, input().split())))
print(*sorted(list(nums)))