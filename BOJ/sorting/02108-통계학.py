from collections import Counter

n = int(input())
li = sorted(list(int(input()) for _ in range(n)))
# 산술평균
print(round(sum(li) / n))
# 중앙값
print(li[n // 2])
# 최빈값
cnt = Counter(li).most_common(2)
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
# 범위
print(li[-1] - li[0])
