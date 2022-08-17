# reverse=True 자주 안 쓰다보니까 까먹었다 그새 ^^;; 으이가 음네

# 풀이 1

n, k = map(int, input().split())
li = sorted(list(map(int, input().split())))

print(li[-k])


# 풀이 2 

n, k = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)

print(li[k - 1])