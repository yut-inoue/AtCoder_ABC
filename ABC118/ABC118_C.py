n=int(input())
#n,m=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

import fractions
#gcd=fractions.gcd(a,b)#最大公約数
#lcm=(a*b)/fractions.gcd(a,b)#最小公倍数
gcd=al[0]
for i in range(1,n):
    gcd=fractions.gcd(gcd,al[i])

print(gcd)
