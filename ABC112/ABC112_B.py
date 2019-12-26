n,t=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
c_l=[]
for i in range(n):
    c_i=l[i][0]
    t_i=l[i][1]
    if t_i<= t:
        c_l.append(c_i)
if len(c_l)==0:
    print("TLE")
else:
    print(min(c_l))

