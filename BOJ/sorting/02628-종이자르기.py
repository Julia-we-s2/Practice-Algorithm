x, y = map(int, input().split())
n = int(input())
x_list = [0, x]
y_list = [0, y]
max_width = 0
max_height = 0

for _ in range(n):
    direction, line = map(int, input().split())
    if direction == 0:
        y_list.append(line)
    else:
        x_list.append(line)

x_list.sort()
y_list.sort()

for i in range(1, len(x_list)):
    if x_list[i] - x_list[i - 1] > max_width:
        max_width = x_list[i] - x_list[i - 1]

for i in range(1, len(y_list)):
    if y_list[i] - y_list[i - 1] > max_height:
        max_height = y_list[i] - y_list[i - 1]

print(max_width * max_height)
