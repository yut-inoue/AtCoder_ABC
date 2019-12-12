n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
flag=True
mx=l[0]
if mx < sum(l[1:n]):
  print("Yes")
else:
  print("No")