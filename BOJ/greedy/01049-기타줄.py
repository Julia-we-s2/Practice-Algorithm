# 가장 저렴한 가격의 값만 찾아주면 된다, 나머지 가격은 저장할 필요 없음 !

# 모두 다 낱개로 사는 게 저렴해? 
# yes - 낱개 * n 
# no - 최대한 패키지로 많은 걸 산 다음 남은 기타줄을 낱개로 사는 게 더 저렴한지 판단
# yes - 낱개 * 남은 개수
# no - 패키지 1 개 더하기

n, m = map(int, input().split())

min_package = 1001
min_individual = 1001

for i in range(m):
    package, individual = map(int, input().split())
    min_package = min(min_package, package)
    min_individual = min(min_individual, individual)

res = 0

if min_package <= min_individual * 6:
    res += (n // 6) * min_package
    if (n % 6) * min_individual > min_package:
        res += min_package
    else:
        res += (n % 6) * min_individual

else:
    res += n * min_individual

print(res)