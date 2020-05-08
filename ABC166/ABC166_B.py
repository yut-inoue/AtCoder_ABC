#n=int(input())
n,k=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

dic={}

for i in range(k):
    d=int(input())
    al=list(map(int,input().split()))
    for a in al:
        dic[a]=True
ans=0
for i in range(1,n+1):
    if dic.get(i,0)==0:
        ans+=1
print(ans)






