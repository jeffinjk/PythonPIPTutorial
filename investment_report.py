print("investment report")
print("---------------------")
start_invest=float(input("Enter the initial investment:"))
annual_return=float(input("Enter the annual return:"))/100
years=int(input("Enter the number of years:"))

current_invest=start_invest

for i in range(1,years+1):
    #current_invest=current_invest+(current_invest*annual_return)
    current_invest=current_invest*(1+annual_return)
    print("Year",i,"investment:",current_invest)
    
print("The final value after", years ,"years is: ",current_invest)
    
    



