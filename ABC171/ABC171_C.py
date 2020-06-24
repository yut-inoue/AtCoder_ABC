n=int(input())
#x,n=map(int,input().split())
#pl=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

res=''

# 文字数を求める
total=0
i=1
while True:
    if total+26**i>=n:
        break
    else:
        total+=26**i
        i+=1

# 文字数iがわかったので，そのなかでn-i番目
k=n-total-1
for j in range(i):
    res+=chr(ord('a')+k%26)
    k=k//26

print(res[::-1])
