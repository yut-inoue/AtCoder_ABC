#n = int(input())
n,m = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
al=[];bl=[]
for i in range(m):
    a,b = map(int,input().split())
    al.append(a)
    bl.append(b)

k=int(input())
cl=[];dl=[]
for i in range(k):
    c,d = map(int,input().split())
    cl.append(c)
    dl.append(d)

ans=0
for i in range(2**k):
    score=0
    dic={}
    for j in range(k):
        if ((i >> j) & 1):
            dic[cl[j]]=1
        else:
            dic[dl[j]]=1
    for ai, bi in zip(al, bl):
        if dic.get(ai, 0)==1 and dic.get(bi, 0)==1 :
            score+=1
    ans=max(score, ans)
print(ans)
