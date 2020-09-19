n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
ans=0
for a in range(1,n+1):
    ans+=(n-1)//a
print(ans)