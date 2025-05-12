def sum_of_digits(n):
    total=0
    while(n>0):
        total+= n%10
        n=n//10
    return total

for num in range(100,1001):
    if sum_of_digits(num) %9==0:
        print(num)
        