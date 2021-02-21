#n = int(input())
n,k = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

def digit(n):
    res = []
    while n > 0:
        res.append(n % 10)
        n = n//10
    return res

def asnum(l):
    i=0
    for i in range(len(l)):
        if l[i]==0:
            pass
        else:
            break
    l=l[i: ]
    n=len(l)
    res=0
    for i in range(n):
        res+=(10**i)*l.pop(-1)

    return res

aibef=n
for i in range(1, k+1):
    #g1
    g1=digit(aibef)
    g1.sort(reverse=True)

    g2=digit(aibef)
    g2.sort()

    aibef=asnum(g1)-asnum(g2)

print(aibef)