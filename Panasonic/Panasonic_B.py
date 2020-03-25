#n=int(input())
h,w=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
m=h//2
n=w//2

if h==1 or w==1:
    ans=1
elif h%2==0:
    ans=m*w
else:
    md=w%2
    ans=n*(m+1+m)+md*(m+1)
print(ans)