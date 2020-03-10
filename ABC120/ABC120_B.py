#n=int(input())
a,b,k=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
l=[]
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        l.append(i)

l.sort(reverse=True)

print(l[k-1])
