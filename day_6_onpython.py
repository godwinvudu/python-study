#whileloop
name=input("enter your name:")
while name=="":
    print("you did not enter your name:")
    name=input("enter your name:")
    print(f"hello {name}")
     

#whileloop 

#reading inputs in a while loop
info=input("enter begin:")
while info !="begin":
    input("Wrong.Enter begin:")

    (print("The while loop condition has been met"))


#sum odd numbers between inputs
n1=int(input("input the first number:"))
n2=int(input("input second number"))
#odd numbers between the two integers
total=0
#This is very important.
#You need a variable to store the running sum.
#Think of total like a container that starts empty (0).
while n1<=n2:
    #check if the number is odd
    if n1 %2!=0:
        print(n1)
        #total = total + n1
        total +=n1
    n1+=1
      #This increases n1 by 1 every loop.
    #If we don’t do this, the loop would never move forward (infinite loop).
print(total)   
