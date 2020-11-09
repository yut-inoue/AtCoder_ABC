import itertools
#n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#pl = [list(map(int, input().split())) for i in range(n)]
ans = 'No'
s = input()
n = len(s)
intlist = [i for i in range(1, 10)]
if n > 3:
    l = [8*i for i in range(13, 125)]
    for v in l:
        if all([str(v).count(m) <= s.count(m) for m in set(list(str(v)))]):
            ans = 'Yes'
else:
    for v in itertools.permutations(s, n):
        if int(''.join(v)) % 8 == 0:
            ans = 'Yes'
            break
print(ans)
