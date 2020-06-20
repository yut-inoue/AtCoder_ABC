n=int(input())
#n,m=map(int,input().split())
#t=int(input())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

difl=[al[i-1]-i for i in range(1,n+1)]

def sadness(b):
    res=0
    for dif in difl:
        res+=abs(dif-b)
    return res
difsort=sorted(difl)
if n%2==0:
    ind1=n//2
    ind2=n//2-1
    ans=min(sadness(difsort[ind1]),sadness(difsort[ind2]))
else:
    ind=n//2
    ans=sadness(difsort[ind])
print(ans)