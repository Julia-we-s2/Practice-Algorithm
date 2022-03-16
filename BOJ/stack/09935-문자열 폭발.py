import sys
input = sys.stdin.readline

s = list(input().rstrip())
bomb = list(input().rstrip())

stack = []

for i in range(len(s)):
    stack.append(s[i])

    if len(stack) >= len(bomb) and stack[-1] == bomb[-1]:
        if stack[-len(bomb):] == bomb:
            for i in range(len(bomb)):
                stack.pop()

if stack:
    print("".join(stack))

else:
    print("FRULA")
