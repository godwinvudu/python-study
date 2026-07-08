#strings= a sequence of characters
#modifying strings :Using lower() returns converted alphabet characters to lowercase
#upper() returns converted alphabetical characters to uppercase
#eg
def lower1():
    checkinglower=input("enter something capitalised:").lower()
    print(checkinglower)
lower1()

def upper_1():
    checkingupper=input("enter something but should be in lower case:").upper()
    print(checkingupper)
upper_1()
#index slicing
#when a programmer must get access to a sequence of characters

time_string="12:18666"
minutes=time_string[3:8]
print(minutes)