n = int(input())
li = []
for _ in range(n):
    no = input()

    temp = 0
    for each in str(no):
        if each in '1234567890':
            temp += int(each)

    li.append((no, temp, len(no)))

li.sort(key=lambda x: (x[2], x[1], x[0]))

for each in li:
    print(each[0])
    