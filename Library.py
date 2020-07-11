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
#フェルマーの小定理で逆元を求める modpowを使っている！
def modinv(a,mod):
    return modpow(a,mod-2,mod)
###############################################
#nCkをmodで割ったあまり note: k=0なら1を返すように場合分けが必要
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
#素因数分解した結果を2次元配列にして返す
def prime_factorize(n):
    n_origin=n+0
    primelist=[]
    a=2
    while a*a<=n_origin:
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
###################################################
#オイラーのファイ関数
#1~n の整数のうち，nと互いに素なものの個数を求める

###################################################
#約数を列挙するO(sqrt(n))
def enum_divisors(n):
    res=[]
    i=1
    while i*i<=n:
        if n%i==0:
            res.append(i)
            if n//i!=i:
                res.append(n//i)
        i+=1
    res.sort()
    return res
###################################################
#bit全探索
for i in range(2**n):
    b=bin(i)
    for j in range(n):
        if ((i >> j) & 1):#二進数iの下から数えてj桁目が1か否か
            # もしj番目をとるなら
            pass

###################################################
# 再帰関数のテンプレ DFS
m=2
def dfs(A):
    if len(A)==3:
        print(A)
        return
    for v in range(m):
        A.append(v)
        dfs(A)
        A.pop()
dfs([])

###################################################
# 配列の二分探索
def binary_search(A,key):
    left=0
    right=len(A)-1
    while left<right:
        mid=(left+right)//2
        if A[mid]==key:
            return mid
        elif key<A[mid]:
            right=mid
        else:
            left=mid+1
    return False
# bisectを使っても同じようにできる
import bisect
A=[1,2,3,4,5]
key=1
ind=bisect.bisect_left(A,key)
if ind>len(A)-1:# もしkeyが配列の最大値よりも大きいなら
    print("not found")
elif A[ind]==key:
    print("found")
else:
    print("not found")

# 正整数nに対して単調増加の関数の二分探索
# f(n)<=x となる最大のnを返す
# 二分探索は，f(n)>=xとなる最小のnを求める際にも適用できる
left=0;right=10**9+1
while right-left>1:
    mid=(left+right)//2
    if f(mid)>x:
        right=mid
    else:
        left=mid
# 最終的にleftが答え

############################################
# 入力vをaで何回割り切れるか
def div2(v,a):
    res=0
    if v==0:
        return res
    while v%a==0:
        v=v//a
        res+=1
    return res

############################################
# 10-baseの整数vをn進数で表す．
def n_base_digit(v,n):
    res=[]
    while v!=0:
        c=v%n
        res.append(c)
        v=v//n
    res=res[::-1]
    return int(''.join(map(str,res)))