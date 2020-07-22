n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
l=[2,1]
for i in range(2,n+2):
    l.append(l[i-1]+l[i-2])
print(l[n])