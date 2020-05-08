#n=int(input())
n,m,q=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

al=[]
bl=[]
cl=[]
dl=[]
l=[]
ansl=[0 for i in range(n+1)]
for i in range(q):
    a,b,c,d=map(int,input().split())
    al.append(a)
    bl.append(b)
    cl.append(c)
    dl.append(d)
    l.append([a,b,c,d])

def score(seq):
    temp=0
    for a,b,c,d in zip(al,bl,cl,dl):
        if seq[b-1]-seq[a-1]==c:
            temp+=d
    return temp

def dfs(seq):
    if len(seq)==n:
        return score(seq)
    res=0
    prev_last=seq[-1] if len(seq)>0 else 1
    for v in range(prev_last,m+1):
        seq.append(v)
        res=max(res,dfs(seq))
        seq.pop()
    return res
print(dfs([]))



