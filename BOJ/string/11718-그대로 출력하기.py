# 쉬운 문제를 얕볼 게 아니다
# 몇 번 입력이 주어지는지 모르기에 try except 구문을 사용해서 입력이 없을 때 멈춘다

while True:
    try:
        print(input())
    except:
        break
