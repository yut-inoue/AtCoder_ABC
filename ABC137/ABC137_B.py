#n=int(input())
k,x=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

l=[i for i in range(max(x-k+1,-1000000),min(x+k-1,1000000)+1)]

print(*l,sep=" ")
