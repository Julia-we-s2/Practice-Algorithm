# set (집합) 의 특징:
# 순서가 없다 -> 인덱싱 지원하지 않는다
# 중복 허용하지 않는다

a, b = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

print(len(set_a - set_b) + len(set_b - set_a))
