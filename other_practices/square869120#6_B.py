n=int(input())
al=[0]*n
bl=[0]*n
for i in range(n):
    al[i], bl[i] = map(int,input().split())
al.sort();bl.sort()
def f(start,end):
    res=0
    for ai,bi in zip(al,bl):
        res+=abs(ai-start)+abs(bi-end)+(bi-ai)
    return res

if n % 2 ==0:
    ans=min(
        f(al[n//2],bl[n//2]),
        f(al[n//2],bl[n//2-1]),
        f(al[n//2-1],bl[n//2]),
        f(al[n//2-1],bl[n//2]-1)
    )
else:
    ans=f(al[(n-1)//2],bl[(n-1)//2])
print(ans)