#n = int(input())
a, b, c, d = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]

print(max(0, min(b, d)-max(a, c)))
