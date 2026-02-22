#Nested loops-has one or more loops within the body of another loop
 #outer loop:
   #inner loop
#try it :print a triangle of numbers
# end="" tells the computer "don't go to the next line yet".so code doesn't move to the next line until iteration is done

sentence=input("enter sentence: ")
count=0
for c in sentence:
  if c ==" ":
     count+=1
print(count)


number1=int(input("enter first number: "))
number2=int(input("enter second number: "))

for i in range(number1,number2+1):
  if i%2==0:
    print(i,end=" ")
print()
for e in range (number1,number2):
  if e%2!=0:
   print(e,end=" ") 
print()
i=1
while i<=5:
    j=1
    while i + j <=5:
        print(i, j)
        j +=1
    i+=1

#print()-moves the cursor to the next line at the end of the final iteration
