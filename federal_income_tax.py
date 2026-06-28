def main():
    print("This code calculates the taxable income of individuals ")
    print(" ")
    income=(int(input("how much do you make?")))
    if income <=9_875:
        tax=income*0.1
        bracket="10%"
    elif income<=40_125:
        tax=987.5+(income-9_875)*0.12
        bracket="12%"
    elif income<=85_525:
        tax=4_617.50+(income-40_125)*.22
        bracket="22%"
    elif income<=163_300:
        tax=14_605.50+(income-85_525)*0.24
        bracket="24%"
    else :
        tax=14_605.50+(income-163_300)*0.32
        brackets="32%"
    
    print(f"if your in come is {income} your tax is {tax} in the bracket of {bracket}")

main()

