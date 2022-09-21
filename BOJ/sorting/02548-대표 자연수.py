n = int(input())
nums = sorted(list(map(int, input().split())))

a, b = divmod(n, 2)
print(nums[a + b - 1])
