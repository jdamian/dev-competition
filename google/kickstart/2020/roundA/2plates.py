t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  n, k, p = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
  a = [int(s) for s in input().split(" ")] # read ai
  a.sort()
  total = 0
  costoTotal = 0
  for precio in a:
    costoTotal += precio
    if costoTotal <= m :
      total += 1
    else:
      break
  
  print("Case #{}: {}".format(i,total))


