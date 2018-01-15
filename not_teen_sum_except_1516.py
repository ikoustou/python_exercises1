def fix_teen(n):
  if n>=13 and n<=19 :
    if n!=15 and n!=16:
      return 0
    else:
      return n
  else:
    return n

def no_teen_sum(a, b, c):
  l=[a,b,c]
  sum=0
  for item in l:
    sum+= fix_teen(item)
  return sum