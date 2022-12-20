def check(cur, total, cnt):
    if cnt == n:
        nums.add(total)
        return

    for i in range(cur, 4):
        check(i, total + infos_index[i], cnt + 1)


nums = set()
infos_index = [1, 5, 10, 50]
n = int(input())
check(0, 0, 0)
print(len(nums))
