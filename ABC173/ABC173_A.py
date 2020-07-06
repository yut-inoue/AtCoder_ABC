n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
v=n//1000
mod=n%1000
if mod==0:
    ans=0
else:
    ans=(v+1)*1000-n
print(ans)