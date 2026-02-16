print("welcome to wicked girl's(beryl) banking system")
name=input("enter name:")
pin=int(input("enter pin: "))
balance=2000000
while [name]+[pin]!=["beryl"]+[1234]:
    name=input("wrong pin or password\n"
               "enter name: ")
    pin=int(input("enter pin: "))

print(f'welcome {name}')    
option=int(input("Choose servise\n"
      "1.Check balence\n"
      "2.Withdraw\n"
      "3.Deposit\n"
      "4.Transfer to another cutomer\n"
      "5.log out\n"
      ":") )  

if  option==1:
    print(f' wicked girl,your balance is {balance}')
elif option==2:
    withdraw=int(input("enter withdraw amount: "))
    while withdraw > balance:
       withdraw=int(input("withdraw amount invalid.\n"
       "enter withdraw amount: "))
    print("withdraw succesful")   
    while withdraw<0:
        withdraw=int(input("withdraw amount invalid.\n"
       "enter withdraw amount: "))
elif option==3:
    deposit=input("enter  account number for deposit: ") 
    deposit_amount=int(input("enter deposit amout: "))
    while deposit_amount<0 and deposit_amount>balance:
        deposit_amount=int(input("enter deposit amout: "))
elif option==4:
    customer_account=input("enter customer account: ")
    customer_amount=int(input("enter transfer amount: "))        
    while customer_amount<0 and customer_amount>balance:
        customer_amount=int(input("enter deposit amout: "))
elif option==5:
    print("loging out now \U0001F595")








