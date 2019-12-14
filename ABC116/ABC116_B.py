s=int(input())

def f(n):
  if n%2==0:
    return n/2
  else:
    return 3*n+1

l=[s]
m=0
before=s
while True:
  new=f(before)
  m+=1
  if new in l:
    break
  l.append(new)
  before=new

print(m+1)
