n=0

#順列と組み合わせ
#単なる計算math
import math
fac=math.factorial(n)#n!を返す
def permutations_count(n, r):#nPrを返す
    if r<0 or r>n:
        return 0
    elif r==0:
        return 1
    else:
        return math.factorial(n) // math.factorial(n - r)

#nCkを返す
def combinations_count(n,k):
    if k==0 or k==n:
        return 1
    elif n<k or k<0:
        return 0
    else:
        return math.factorial(n)//(math.factorial(n-k)*math.factorial(k))

def combinations_with_replacement_count(n, r):
    #重複組み合わせn個から重複を許してr個選ぶ
    return combinations_count(n + r - 1, r)
################################################
#a^nをmodでわったあまり 二分累乗法O(logn)
def modpow(a,n,mod):
    res=1
    while n>0:
        if n&1:
            res=(res*a)%mod
        a=(a*a)%mod
        n=n>>1
    return res
#################################################
#a!をmodで割ったあまりを求めるO(a)
def facmod(a,mod):
    res=1
    for i in range(1,a+1):
        res=(res*i)%mod
    return res
#################################################
#フェルマーの小定理で逆元を求める
def modinv(a,mod):
    return modpow(a,mod-2,mod)
###############################################
#nCkをmodで割ったあまり
#テーブルを作る前処理
mod=10**9+7
fac=[0,1]
finv=[0,1]
inv=[0,1]
for i in range(2,n+1):
    fac.append(fac[i-1]*i%mod)
    inv.append(mod-inv[mod%i]*(mod//i)%mod)
    finv.append(finv[i-1]*inv[i]%mod)
#二項係数計算部分
def combinations_mod(n,k,mod):
    if n<k:
        return 0
    if n<0 or k<0 :
        return 0
    return fac[n]*(finv[k]*finv[n-k]%mod)%mod
#################################################
#bit全探索
for i in range(2**n):
  b=bin(i)
  for j in range(n):
    if ((i >> j) & 1):#二進数iの下から数えてj桁目が1か否か
        pass
