#n=int(input())
n,m=map(int,input().split())
hl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
dic={}
for i in range(n):
    dic[i+1]=True
for i in range(m):
    a,b=map(int,input().split())
    if hl[a-1]<=hl[b-1]:
        dic[a]=False
    if hl[b-1]<=hl[a-1]:
        dic[b]=False
ans=0
for k,v in dic.items():
    if v :
        ans+=1

print(ans)





