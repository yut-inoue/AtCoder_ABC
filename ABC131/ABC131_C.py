a,b,c,d=map(int,input().split())
import fractions
#cとdの最小公倍数
lcm=c*d//fractions.gcd(c,d)
count1=b-(b//c+b//d-b//lcm)
count2=(a-1)-((a-1)//c+(a-1)//d-(a-1)//lcm)

print(count1-count2)
