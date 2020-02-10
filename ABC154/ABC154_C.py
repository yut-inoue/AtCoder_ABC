n=int(input())
al=list(map(int,input().split()))

dic={}
flag=True
for i in range(n):
    v=al[i]
    dic[v]=dic.get(v,0)+1
    if dic[v]==2:
        flag=False
        break
if flag:
    print("YES")
else:
    print("NO")
