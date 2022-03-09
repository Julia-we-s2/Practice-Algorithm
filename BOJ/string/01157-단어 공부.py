# 풀이 1: 딕셔너리 활용

word = input()
dic = {}
most_frequently = -1
ans = []

for i in word:
    i = i.lower()
    if i.lower() not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for i in dic:
    if dic[i] > most_frequently:
        most_frequently = dic[i]

for i in dic:
    if dic[i] == most_frequently:
        ans.append(i)

if len(ans) > 1:
    print("?")
else:
    print(ans[0].upper())

