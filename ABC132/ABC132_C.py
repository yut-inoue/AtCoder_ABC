n=int(input())
#a,b=map(int,input().split())
dl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
ans=1
dl.sort()
if n%2==0:
    mid=n//2
    ans=dl[mid]-dl[mid-1]
print(ans)    
