while True:
  li = list(map(int, input().split()))
  li.sort()
  a, b, c = li
 
  if a == 0 and b == 0 and c == 0:
    break
  
  if c ** 2 == b ** 2 + a ** 2:
    print("right")
  else:
    print("wrong")
