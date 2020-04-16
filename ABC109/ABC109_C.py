#n=int(input())
n,x=map(int,input().split())
xl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

import fractions
#gcd=fractions.gcd(a,b)#最大公約数
#lcm=(a//fractions.gcd(a,b))*b #最小公倍数

res=0

for i in range(n):
    res=fractions.gcd(res,abs(x-xl[i]))

print(res)


