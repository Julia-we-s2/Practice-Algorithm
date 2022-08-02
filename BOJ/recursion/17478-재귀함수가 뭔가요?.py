# 내 첫 재귀함수 폴더의 문제.. 귀엽군 <3
# 얼마 전에는 재귀 넘넘 어려웠는데, 조금은 익숙해진 거 같아서 기부니 좋다 

def repeat_chatbot(repetition_time):
    print('____' * repetition_time + '"재귀함수가 뭔가요?"')

    if repetition_time == n:
        print('____' * repetition_time + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print('____' * repetition_time + '라고 답변하였지.')
        return

    print('____' * repetition_time + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print('____' * repetition_time + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print('____' * repetition_time + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    repeat_chatbot(repetition_time + 1)
    print('____' * repetition_time + '라고 답변하였지.')


n = int(input())
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
repeat_chatbot(0)
