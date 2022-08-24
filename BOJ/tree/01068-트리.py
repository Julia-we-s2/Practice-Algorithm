def dfs(num, li):
    li[num] = -2
    for i in range(len(li)):
        if num == li[i]:
            dfs(i, li)


n = int(input())
li = list(map(int, input().split()))
delete_node = int(input())
cnt = 0

dfs(delete_node, li)

cnt = 0
for i in range(len(li)):
    if li[i] != -2 and i not in li:
        cnt += 1

print(cnt)