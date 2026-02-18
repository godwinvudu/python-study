sentence=input("Enter sentence: ")
count=0
for i in sentence:
    if i==" ":
     count+=1
print(count)
     

n1=int(input("input first number: "))
n2=int(input("Enter second number: "))
if n1<n2:
   print("second number should be larger than first:")
for num in range(n1,n2+1):
   if num%2==0:
      print(num)