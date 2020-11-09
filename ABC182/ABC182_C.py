#n = int(input())
#a, b = map(int,input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
n = input()
k = len(n)
ans = -1
for i in range(2**k):
    b = bin(i)
    count = 0
    temp = ''
    for j in range(k):
        if ((i >> j) & 1):  # 二進数iの下から数えてj桁目が1か否か
            temp += n[j]
            count += 1
    if count == 0:
        continue
    temp = int(temp)
    if temp % 3 == 0:
        if ans == -1:
            ans = k-count
        else:
            ans = min(ans, k-count)
print(ans)
