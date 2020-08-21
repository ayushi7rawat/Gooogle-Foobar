def solution(xs):
  res1 = []
  res2=[]

  #append -ve elements in res1 and +ve in res2
  for i in xs:
    if i>0:
      res1.append(i)
    if i<0:
      res2.append(i)

  #if both empty then we only have zero(s)
  if res1 ==[] and res2 == []:
    return str(0)

  if res1 == [] and len(res2)==1:
    #when only 1 -ve element is present
    if len(xs) == 1:
      return str(xs[0])
    # when 1 -ve and other are zero(s)
    return str(0)

  #when we have odd num of -ve num
  if len(res2)%2!=0:
    res2.sort()
    res2.pop()

  product=1
  for i in (res1+res2):
    product*=i

  return str(product)