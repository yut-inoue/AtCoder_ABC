#n=int(input())
a,b,c,k=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

if k<=a+b:
    ans=min(a,k)
else:
    ans=a-(k-(a+b))

print(ans)


