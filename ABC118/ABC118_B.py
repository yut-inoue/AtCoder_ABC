n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]

dic={}
for i in range(1,m+1):
  dic[i]=0
ans=0
for i in range(n):
  k=l[i][0]
  templ=l[i][1:k+1]
  for a in templ:
    dic[a]=dic[a]+1
for v in dic.values():
  if v==n:
    ans+=1
print(ans)