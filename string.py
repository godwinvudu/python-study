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
def x():
    x='192:67'
    x="2" +x[1:]#replacing the first character of the string
    print(x)
x()
str = "morning" 
str = str[1] 
print(str)
#in operator
a="umbrella"
b="a"in a
q="z" in a
print(b)
print(q)
#in in loops(for)
for n in "string": 
  print(n, end = " ") 
# 

  count = 0 
for c in "abca": 
  if c == "a": 
    count += 1 
print(count)