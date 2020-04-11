a,b=map(int,input().split())

#素因数分解した結果を2次元配列にして返す
def prime_factorize(n):
    primelist=[]
    a=2
    while a*a<=n:
        if n%a!=0:
            a+=1
            continue
        ex=0
        while n%a==0:
            ex+=1
            n=n//a
        primelist.append([a,ex])
        a+=1
    if n!=1:
        primelist.append([n,1])
    return primelist

import fractions
g=fractions.gcd(a,b)

pfs=prime_factorize(g)

print(1+len(pfs))

