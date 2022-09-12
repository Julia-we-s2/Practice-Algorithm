n = int(input())
nums = set(range(1, n+1))
cnt = 0
li = []


def check_sequence(a):
    print(a)
    global cnt
    if int(a[1]) - int(a[0]) == int(a[2]) - int(a[1]):
        cnt += 1


for num in nums:
    if num < 100:
        cnt += 1
    else:
        for i in str(num):
            li.append(i)
        check_sequence(li)
        li = []

print(cnt)