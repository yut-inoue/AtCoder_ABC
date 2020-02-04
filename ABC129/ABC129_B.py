n=int(input())
wl=list(map(int,input().split()))

dif=[]

for t in range(n):
    dif.append(abs(sum(wl[0:t+1])-sum(wl[t+1:n])))
print(min(dif))

