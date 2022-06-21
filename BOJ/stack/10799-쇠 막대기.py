# 괄호를 확인할 떄 temp 가 아닌 brackets 에서 확인 해야하는 거 조심 !
# ')' + ')' 인 경우는 쇠막대기가 끝나는 지점을 의미하니까 + 1

brackets = list(input())
temp = []
cnt = 0

for i in range(len(brackets)):
    if brackets[i] == '(':
        temp.append('(')

    else:
        if brackets[i - 1] == '(':
            temp.pop()
            cnt += len(temp)

        else:
            temp.pop()
            cnt += 1

print(cnt)
