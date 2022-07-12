# 풀이 1: 배열을 합쳐서 정렬하기

n, m = map(int, input().split())
a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))

print(*sorted(a_li + b_li))



# 풀이 2: 투 포인터를 이용하여 merge sort 하기 

n, m = map(int, input().split())
a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))
ans = []
a, b = 0, 0

while a != len(a_li) or b != len(b_li):
    if a == len(a_li):
        ans.append(b_li[b])
        b += 1
    elif b == len(b_li):
        ans.append(a_li[a])
        a += 1

    else:
        if a_li[a] < b_li[b]:
            ans.append(a_li[a])
            a += 1
        else:
            ans.append(b_li[b])
            b += 1

print(*ans)