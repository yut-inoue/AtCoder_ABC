#n = int(input())
w, h = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

# nCkをmodで割ったあまり note: k=0なら1を返すように場合分けが必要
# テーブルを作る前処理
mod = 10**9+7
fac = [0, 1]
finv = [0, 1]
inv = [0, 1]
for i in range(2, h+w+1):
    fac.append(fac[i-1]*i % mod)
    inv.append(mod-inv[mod % i]*(mod//i) % mod)
    finv.append(finv[i-1]*inv[i] % mod)


def combinations_mod(n, k, mod):  # 二項係数計算部分
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n]*(finv[k]*finv[n-k] % mod) % mod
print(combinations_mod(h+w-2, h-1, mod))