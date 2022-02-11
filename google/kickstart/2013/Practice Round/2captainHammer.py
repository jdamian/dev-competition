from math import sqrt, atan, degrees
from decimal import *

t= int(input())

for i in range(1, t + 1):
  result, r1, r2 = 0, 0, 0
  v, d = [int(s) for s in input().split(" ")]
  g = 9.8

  a = ((-((g*d*d)/(2*v*v))))
  b = d
  c = a

  r1 = (-b - sqrt(b*b-int(4*a*c)))/(2*a)
  r2 = (-b + sqrt(b*b-int(4*a*c)))/(2*a)

  if r1 < 0:
    result = degrees( atan(r2))
  elif r2 < 0:
    result = degrees( atan(r1))
  elif r1 < r2:
    result = degrees( atan(r1))
  else:
    result = degrees( atan(r2))

  print("Case #{}: {:.9f}".format(i, result))

  