#for loops
#a for loop is used to repeat something a specific number times or go through items in a list
#it executes a block of code a fixed number of times 
#you can iterate over a range ,string ,sequence ,etc 
#iteration means repeating something over and over
str_var="a string"
count=0
for c in str_var:
    count +=2
print(count)    
#c is the variable name,it stores each item during each iteration of the loop.
#the are 8 characters in "a string" (including the gap) 
#it can be renamed

str_var="string"
count=0
for banana in str_var:
     count +=3
print(count)    

#counting in a for loop.
#a range function generates a sequence  of integers between the two numbers given a step size
#its inclusive of start and exclusive of the end of the sequence
#eg
range(4)
#prints 0,1,2,3
range(1,4)
#prints 1,2,3
range(2,7,2)
#prints 2,4,6

#try it
str=input("enter a string: ")
count=0
for i in str:
    if str=="":
        count +=1
        print(count)
#try it sequences
n1=int(input("enter first number: "))
n2=int(input("enter second number: "))
while n1>n2:
    n2=int(input("second number should be greater than first: "))
n=range(n1,n2+1) 
count=0
for c in n:
    if c %2==0:
        print(c)
        count+=1
        