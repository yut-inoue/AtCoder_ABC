#n=int(input())
n,a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
mod=1000000007
def binary(n):
    return bin(n)[2:]
def pow_by_binary_exponentiation(a, x, n): # a^x mod n
    x = [int(b) for b in binary(x)]
    y = a
    for i in range(1, len(x)):
        y = (y**2) % n
        if x[i] == 1:
            y = (y * a) % n
    return y

ans=pow_by_binary_exponentiation(2,n,mod)

ans=(ans-1)%mod

mx=min(n,2*(10**5))
fac=[1,1]

finv=[1,1]
inv=[0,1]

for i in range(2,mx):
    fac.append(fac[i - 1] * i % mod)
    inv.append(mod - inv[mod%i] * (mod / i) % mod)
    finv.append(finv[i - 1] * inv[i] % mod)

#二項係数を計算する
def COM(n,k):
    if n<k:
        return 0
    if n<0 or k<0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod

nca=COM(n,a)
ans=(ans-nca)%mod

ncb=COM(n,b)
ans=(ans-ncb)%mod

print(ans)