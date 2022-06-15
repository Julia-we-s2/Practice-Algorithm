# 인덱스들 중 대략 중간에 위치한 인덱스로 접근한 후 그 위치의 값을 보는 것 !
# (인덱스로 통해 nums 리스트의 원소에 접근을 해야지 
# 그냥 숫자로 접근을 해버리게 되면 nums 리스트에 들어있지도 않는 값으로 뜬금 접근을 하게 되잖아 ,,,)  

# 원소의 값이 0일 수도 있으니까 return 을 0으로 해버리면 안 돼 !

import sys
input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))
m = int(input())
check_nums = list(map(int, input().split()))


def binary_search(target):
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False


for i in range(m):
    if binary_search(check_nums[i]):
        print(1, end=' ')
    else:
        print(0, end=' ')
