#n = int(input())
n, k = map(int, input().split())
#al = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
hl = [int(input()) for i in range(n)]

hl.sort()
mn = hl[k-1]-hl[0]
for i in range(n-k+1):
    mn = min(mn, hl[i+k-1]-hl[i])
print(mn)
