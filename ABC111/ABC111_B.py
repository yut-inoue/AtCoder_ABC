n=int(input())

while True:
    l=list(str(n))
    if l[0]==l[1] and l[1]==l[2]:
        break
    n+=1
print(n)

