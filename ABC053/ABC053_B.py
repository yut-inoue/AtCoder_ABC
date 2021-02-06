#n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
s=list(input())
aind=s.index('A')
for i in range(len(s)):
    if s[i]=='Z':
        zind=i
print(zind-aind+1)