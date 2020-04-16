n=int(input())
ans="Yes"
dic={}
w=input()
last=w[-1]
dic[w]=dic.get(w,0)+1
for i in range(n-1):
    w=input()
    if dic.get(w,0)==1 or w[0]!=last:
        ans="No"
        break
    dic[w]=dic.get(w,0)+1
    last=w[-1]

print(ans)



