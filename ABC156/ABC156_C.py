n=int(input())
#a,b=map(int,input().split())
xl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]


mn=min(xl)
mx=max(xl)
dis=[]
for p in range(mn,mx+1):
    total=0
    for i in range(n):
        total+=(xl[i]-p)**2
    dis.append(total)
print(min(dis))

