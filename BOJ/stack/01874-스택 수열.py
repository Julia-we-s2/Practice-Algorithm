# 되게 신기하고 재밌었던 문제였다 

# cur 의 초기값을 1로 설정하는 것도 신경 써야 한다 !
# e.g.) 4를 스택에 넣고 바로 pop 해야하는 경우,
# 1을 더해서 cur 를 5로 유지한 채 해당 값을 스택에는 집어넣지 않을 수 있다

# for 문이 도는 것은 1~ n 까지의 수가 아닌 n 개의 입력값들이다

# 다른 값들 + 'NO' 가 답으로 나오면 오답이기에
# 이런 경우를 방지하고자 값들을 일단 res 리스트에 담야줘야 한다

n = int(input())
st = []
cur = 1
res = []

for i in range(n):
    num = int(input())

    while cur <= num:
        st.append(cur)
        res.append('+')
        cur += 1
    if st[-1] == num:
        st.pop()
        res.append('-')
    else:
        res.append('NO')
        break
      
if 'NO' in res:
    print('NO')
else:
    for i in res:
        print(i)
