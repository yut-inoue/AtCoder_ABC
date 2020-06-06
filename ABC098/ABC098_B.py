n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
s=list(input())
mx=0
for i in range(1,n):
    l1=s[0:i];l2=s[i:n]
    mx=max(mx,len(set(l1) & set(l2)))

print(mx)
