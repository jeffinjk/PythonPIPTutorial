def primenum(n):
    if n<2:
        return False
    for i in range(2,int(n/2)):
        if n%i==0:
            return False 
    return True
    

for i in range (2,50):
    if primenum(i):
        print(i)
    
            
        
