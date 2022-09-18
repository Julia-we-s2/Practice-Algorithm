n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]

numerator = 1
denominator = 1

for i in nums[-m:]:
    numerator *= i

for i in nums[:m]:
    denominator *= i

print(numerator // denominator)