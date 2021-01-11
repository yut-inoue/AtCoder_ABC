n = int(input())
#a, b = map(int,input().split())
al = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

def winner(l):
    n=len(l)
    res=[]
    for i in range(n):
        if i%2==0:
            res.append(max(l[i], l[i+1]))
    return res


length=2**n
count_dic={}
for i in range(length):
    count_dic[al[i]]=i

take=al
while True:
    if len(take)<=2:
        break
    take=winner(take)

print(count_dic[min(take[0], take[1])]+1)