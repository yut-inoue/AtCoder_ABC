d=int(input())
#n,k=map(int,input().split())
#hl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

st = 'Christmas'

for i in range(abs(d-25)):
    st += ' Eve'

print(st)