def solution(area):
'''
Problem Name: Google Foobar - Solar Doomsday
Author: Ayushi Rawat
'''
  import math
  res = []

  while (area > 0):
    square_root = int(math.sqrt(area))
    val = pow(square_root, 2)
    res.append(val)
    area -= val
  return res