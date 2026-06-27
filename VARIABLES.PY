#variable=named storage location in a computers memory that holds a value that can change
x=12
y=6
w=x+y
print(w)
#pointer stores a memory address of a variable
for i in reversed(range (1,20)):
    print (i)

#python data types ;strings ,numbers,lists,tuples,dictionary,sets,boolean.
#class is another name for data type
print(id(x))
#mutable vs immutable data types
#immutable data types are data types whose value CANNIT BE CHANGED by the programmer after you create it e.g  numbers,strings
#mutable value is one that can be changed
#float division 
x=2/5
print(x)
#floor division
y=15//5
print(y)
#remainder
print(15%2)
#calculating bmi excercise
mass=120
height=2.2
bmi=mass/(height**2)
print(bmi)
print("")

#asking for an input
name=input("enter name:")
print(f"hello {name}")
print("")
age=int(input("how old are you ?"))
print(f"you're {age}")
print("")
#augmented assignment operaators
x=7
x*=7
print(x)
print("")
#another example
l=7
l+=8
print(l)
#simultaneous assignments
print(" ")
m,n=2,3
y,i=3,4
z=m,n*y,i
print(z)
