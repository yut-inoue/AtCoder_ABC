# n=int(input())
d, g = map(int, input().split())
# l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
pl = [0]*d
cl = [0]*d

for i in range(d):
    pl[i], cl[i] = map(int, input().split())
mn = sum(pl)
for i in range(2**d):
    b = bin(i)
    score = 0
    solvenum = 0
    mxp = [_ for _ in range(d)]
    for j in range(d):
        if ((i >> j) & 1):  # 二進数iの下から数えてj桁目が1か否か
            score += pl[j]*(j+1)*100+cl[j]
            solvenum += pl[j]
            mxp.remove(j)
    if score >= g:
        mn = min(mn, solvenum)
    else:
        dif = g - score
        mxp = max(mxp)
        if (mxp+1)*100*(pl[mxp]-1) >= dif:
            solvenum += (dif+((mxp+1)*100)-1)//((mxp+1)*100)
            mn = min(mn, solvenum)

print(mn)
