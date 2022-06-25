import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
ans = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and li[stack[-1]] < li[i]:
        ans[stack.pop()] = li[i]
    stack.append(i)

print(*ans)
