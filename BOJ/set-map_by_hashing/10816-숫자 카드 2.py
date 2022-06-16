# 숫자 리스트를 딕셔너리로 받는 방법이 바로 떠오르지 않았다 ㅇ_ㅇ
# 딕셔너리 자료형에 대해 공부해야 겠군여 ,, 

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

dic = {}

for i in nums:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in check:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')