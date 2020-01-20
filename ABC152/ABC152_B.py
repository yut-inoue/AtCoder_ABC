a,b=map(int,input().split())
a_str=""
b_str=""
for s in range(a):
    a_str+=str(b)
for s in range(b):
    b_str+=str(a)

if a_str<=b_str:
    print(a_str)
else:
    print(b_str)
