# 순회가 고정되지 않은 경우 while

document = input()
check = input()

cnt = 0
i = 0

while i <= len(document) - len(check):
    if document[i:i + len(check)] == check:
        cnt += 1
        i += len(check)
    else:
        i += 1

print(cnt)
