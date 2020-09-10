#Program that allows user access to two different financial calculators

#Import math functions 
import math

print('''Choose either 'Investment' or 'bond' from the menu below to proceed:
-----|Investment|-----  to calculate the amount of interest you'll earn in interest
-------|Bond|-------    to calculate the amount you'll have to pay on a home loan''')

#Input from user starts conditional statements
invest_or_bond = input(str("Please enter Investment or Bond\n" )).lower()
if invest_or_bond  == "investment":
    if True:
        p = float(input("How much are you depositing?\nR")) 
        r = float(input("At which interest rate percentile?\n" )) 
        r = r/100
        t = float(input("How many years are you planning to invest for? \n"))
        #Two types of interest is worked out based on user input  
        simp_comp = str(input("Choose 'Simple' or 'Compound' interest. \n")).lower() 
        if simp_comp == "simple":
            "simple" == simp_comp
            simp_comp = p*(1 + r * t) 
            total = simp_comp
            print (f"Your interest earned over {t} years will be R{total:.2f}".format())
        elif simp_comp:
            simp_comp = p*math.pow((1+r),t) 
            total = simp_comp
            print (f"Your interest earned over {t} years will be R{total:.2f}".format()) 

#Bond is another conditional
elif invest_or_bond == "bond":
    if True:
        p = float(input("What is the current value of the house?\nR")) 
        i = float(input("At which interest rate percentile?\n" )) 
        i = i / 100 * (1/12) 
        n = float(input("How many months you plan to repay? \n")) 
        monthly = float(math.floor((i*p)/(1 - (1+i)**(-n)))) 
        print(f"Your monthly repayment will be {monthly:.2f}".format())  

else:
    print("Please enter a valid input. Try again.") 