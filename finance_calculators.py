import math

#obtaining input from user
product_type = str(input("Please select your product type as either Bond or Investment: "))

#distinguishing between two product options
if product_type.upper() == "BOND":
    print(product_type + " - to calculate the amount you'll have to pay on a home loan.")

elif product_type.upper() == "INVESTMENT":
    print(product_type + " - to calculate the amount of interest you'll earn on your investment.")

#displaying error message if product is not within parameters
else: 
    print("Please select either Bond or Investment as a product") 

#Investment chosen as the product choice
if product_type.upper() == "INVESTMENT":  
    quantum= float(input("Please input quantum: "))
    inv_interest= int(input("Please input your annual rate of return: "))
    inv_horizon= float(input("Please input your investment horizon in years: "))
    interest_type= str(input("Please input your interest type as either simple or compounding:"))

#Investments method of interest selected as simple showing output of investment
    if interest_type == "simple":
                    total = quantum * (1 + inv_interest/100*inv_horizon)
                    print(round(total,2))
#Investments method of interest selected as compounding showing output of investment
    if interest_type == "compounding":
                    total = quantum * math.pow((1+inv_interest/100),inv_horizon) 
                    print(round(total,2))

#Bond chosen as the product choice
if product_type.upper() == "BOND":  
    quantum= float(input("Please input present value of home loan: "))
    inv_interest= int(input("Please input interest your home loan is subject to: "))
    inv_months= float(input("Please input your home loan tenure in months: "))
#Calculation of repayment per month
    repayment = (inv_interest/12/100 * quantum)/(1-(1+inv_interest/12/100)**(-inv_months))
    print(round(repayment,2))






                       

   

    
        