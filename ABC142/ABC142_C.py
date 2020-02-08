n=int(input())
al=list(map(int,input().split()))
l=[0 for i in range(n)]
for i in range(n):
    l[al[i]-1]=str(i+1)
print(" ".join(l))
