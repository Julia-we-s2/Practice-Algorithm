# ' .' 은 문장이고 '.' 은 종료임에 속지 말자 !
# '(' 가 나왔다고 해서 바로 뒤에 오는 원소가 꼭 ')' 일 필요는 없잖어~

while True:
    s = input()
    if s == '.':
        break
    temp = []
    flag = True

    for i in s:
        if i == '(' or i == '[':
            temp.append(i)
        elif i == ')':
            if not temp or temp[-1] == '[':
                flag = False
                break
            else:
                temp.pop()
        elif i == ']':
            if not temp or temp[-1] == '(':
                flag = False
                break
            else:
                temp.pop()
    print('yes' if flag is True and len(temp) == 0 else 'no')
