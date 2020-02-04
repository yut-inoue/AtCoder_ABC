n=int(input())
al=[]
l=[]
for i in range(n):
  a=int(input())
  al.append(a)
  templ=[list(map(int,input().split())) for i in range(a)]
  l.append(templ)
ans=0
for i in range(2**n):
  b=bin(i)
  chkdic={}
  n_honest=0#正直者の人数をカウント
  flag=False#矛盾が生じるかどうか
  for j in range(n):
    if ((i >> j) & 1):#もし正直者なら
      n_honest+=1
      #saying_l=l[j]
      #a=al[j]
      chkdic[j+1]=1
    else:
      chkdic[j+1]=0
  #chkdicをもとに判定
  for j in range(n):
    if ((i >> j) & 1):
      saying_l=l[j]
      a=al[j]
      for k in range(a):
        saying=saying_l[k]
        if chkdic[saying[0]]!=saying[1]:
          flag=True
          break
    if flag:
      break  
  if not flag:
    ans=max(ans,n_honest)
print(ans)
      





