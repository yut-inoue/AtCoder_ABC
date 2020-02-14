n=int(input())
bl=list(map(int,input().split()))
al=[0 for i in range(n)]
al[n-1]=bl[n-2]
for i in range(n-2,-1,-1):
    if al[i+1]>bl[i]:
        al[i+1]=bl[i]
    al[i]=bl[i]
print(sum(al))
