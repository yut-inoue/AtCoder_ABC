x=int(input())
flag=False
for i in range(1,x+1):
    if i*100<=x and x<=105*i:
        flag=True
        break
if flag:
    print(1)
else:
    print(0)
