nums = set(range(1, 10000))
remove_set = set()

for num in nums:
    for i in str(num):
        num += int(i)
    remove_set.add(num)

# set 의 '-' 연산자로 차집합 구하기
self_nums = nums - remove_set

for i in sorted(list(self_nums)):
    print(i)
