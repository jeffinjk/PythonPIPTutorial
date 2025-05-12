def decbin(n):
    bin=""
    while n>0:
        rmdr=n%2
        bin=str(rmdr)+bin
        n=n//2
    return bin if bin else 0 


n=int(input("enter n"))
binres=decbin(n)
print(binres)