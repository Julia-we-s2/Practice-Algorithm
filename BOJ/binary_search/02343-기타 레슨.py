# 이분 탐색: 무엇을 탐색할까 -> 블루레이의 길이
def add_lesson():
    cnt = 0  # 레코드 갯수 세기
    temp = 0  # 한 레코드에 들어갈 레슨의 합

    for i in range(n):
        if temp + li[i] > mid:
            cnt += 1
            temp = 0

        temp += li[i]

    else:
        if temp:
            cnt += 1

    return cnt


n, m = map(int, input().split())
li = list(map(int, input().split()))

start, end = max(li), sum(li)

while start <= end:
    mid = (start + end) // 2
    # 길이가 mid인 블루레이에 담기

    cnt = add_lesson()

    if cnt <= m: # 적거나 같아
        end = mid - 1
    else:
        start = mid + 1

print(start)


