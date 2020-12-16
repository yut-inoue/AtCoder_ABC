#l = int(input())
n, m = map(int, input().split())
al = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

if m == 0:
    ans = 1
elif n == m:
    ans = 0
else:
    al.sort()
    # if al[0]!=1:
    al.insert(0, 0)
    al.append(n+1)
    # if al[-1]!=n
    difl = []
    for i in range(len(al)-1):
        dif = al[i+1]-al[i]-1
        if dif > 0:
            difl.append(dif)
    mn = min(difl)
    ans = 0
    for v in difl:
        ans += (v+mn-1)//mn
print(ans)
