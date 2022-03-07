n = int(input())

triple_six = 666
cnt = 1

while True:
    if cnt == n:
        print(triple_six)
        break

    triple_six += 1

    if '666' in str(triple_six):
        cnt += 1
