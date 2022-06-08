n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
li = []


def dfs():
    if len(li) == m:
        print(' '.join(map(str, li)))
        return

    for i in range(n):
        if nums[i] not in li:
            li.append(nums[i])
            dfs()
            li.pop()


dfs()