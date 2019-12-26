a,b=map(int,input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd (a, b)
#from fractions import lcm
print(lcm(a,b))