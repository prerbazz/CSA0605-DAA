def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
n1=36
n2=24
print("GCD of",n1,"and",n2,"=",gcd(n1,n2))max
