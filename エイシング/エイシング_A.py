#n=int(input())
l,r,d=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
count=0
for i in range(l,r+1):
    if i%d==0:
        count+=1
print(count)