s=input()
k=int(input())

for i in range(len(s)):
    if s[i]!="1":
        nextone=s[i]
        break
if s.count("1")==len(s):
    print(1)
elif i>=k:
    print(1)
else:
    print(nextone)

