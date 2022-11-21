n = int(input())
nums = list(map(int, input().split()))

if n == 1:
    print(sum(nums) - max(nums))
else:
    sum_list = [min(nums[0], nums[5]),
                min(nums[1], nums[4]),
                min(nums[2], nums[3])]
    sum_list.sort()

    one_side = (n - 2) * (n - 2) + (n - 1) * (n - 2) * 4
    two_sides = (n - 2) * 4 + (n - 1) * 4
    three_sides = 4

    ans = one_side * sum_list[0] + two_sides * sum(sum_list[:2]) + three_sides * sum(sum_list)
    print(ans)
