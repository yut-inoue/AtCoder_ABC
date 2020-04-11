n=int(input())
#a,b=map(int,input().split())
vl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

vl.sort()
#ans=(vl[0]+vl[1])/2.0
ans=vl[0]
for i in range(1,n):
    ans=(ans+vl[i])/2

print('{:.9f}'.format(ans))