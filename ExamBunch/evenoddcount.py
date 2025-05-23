n=int(input())
i=0
c_even=0
c_odd=0
while i<=n:
    if i%2==0:
        c_even+=1
    else:
        c_odd+=1
    i+=1    
print("Even Count:",c_even)
print("Odd Count:",c_odd)