n=int(input())
#a,b=map(int,input().split())
pl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
ans=0
for i in range(1,n-1):
    templ=pl[i-1:i+2]
    templ.sort()
    if templ[1]==pl[i]:
        ans+=1
print(ans)
