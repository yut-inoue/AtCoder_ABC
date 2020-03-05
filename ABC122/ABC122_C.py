#n=int(input())
n,q=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
s=list(input())

cuml=[0]
count=0
for i in range(1,n):
    if s[i]=="C" and s[i-1]=="A":
        count+=1    
    cuml.append(count)

ansl=[]
for i in range(q):
    l,r=map(int,input().split())
    if l==1:
        ansl.append(cuml[r-1])
    else:
        ansl.append(cuml[r-1]-cuml[l-1])

for i in range(q):
    print(ansl[i])