n = int(input())
al = list(map(int, input().split()))
q = int(input())
ml = list(map(int, input().split()))
dic = {}
for i in range(2**n):
    res = 0
    for j in range(n):
        if ((i >> j) & 1):
            res += al[j]
    dic[res] = 'yes'
for mi in ml:
    print(dic.get(mi, 'no'))