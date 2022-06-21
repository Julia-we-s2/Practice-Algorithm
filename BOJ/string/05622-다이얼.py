# index(x) 함수는 리스트에 x 값이 있으면 x 의 위치 값을 돌려준다

li = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = input()
cnt = 0

for each in word:
    for i in li:
        if each in i:
            cnt += li.index(i) + 3

print(cnt)
