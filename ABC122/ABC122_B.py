#n=int(input())
#a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]

s=list(input())
n=len(s)
l=["A","C","G","T"]
ansl=[0]
for i in range(n):
    for j in range(n):
        if i>j:
            continue
        partial=s[i:j+1]
        flag=True
        for p in partial:
            if not p in l:
                flag=False
                break
        if flag:
            ansl.append(len(partial))
print(max(ansl))
