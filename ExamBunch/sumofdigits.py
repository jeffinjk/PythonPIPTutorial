def sod(n):
    total=0
    while n>0:
        total+=n%10
        n=n//10
    return total
        
for num in range(100,1001):
    if sod(num)%9==0:
        print(num)
        