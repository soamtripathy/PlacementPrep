from math import sqrt
def checkPerfectNumber( n):
        if n==1:
            return False
        sq=int(sqrt(n))
        s=1
        for i in range(2,sq+1):
            if n%i==0:
                t=n//i
                s+=t+i
        if s==n:
            return True
        return False
print(checkPerfectNumber(28))