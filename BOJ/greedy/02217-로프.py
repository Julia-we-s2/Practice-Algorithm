n = int(input())
li = [int(input()) for _ in range(n)]

li.sort(reverse=True)
rope = []

for i in range(n):
    rope.append(li[i] * (i + 1))

print(max(rope))