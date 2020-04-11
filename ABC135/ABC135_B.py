n=int(input())
#a,b=map(int,input().split())
pl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
#sortedl=sorted(pl)
flag=False
if pl==sorted(pl):
    flag=True
else:
    for i in range(n):
        for j in range(n):
            templ=pl[:]
            templ[i]=pl[j]
            templ[j]=pl[i]
            if templ==(sorted(pl)):
                flag=True
                break
if flag:
    print("YES")
else:
    print("NO")