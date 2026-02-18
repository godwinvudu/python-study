#for loops
for i in range (0,50 +1,5):
    print(i)
sentence=input("enter a sentence: ")
count=0
for c in sentence:
    if c==" ":
        count+=1
print(count)

n1=int(input("input first number"))
n2=int(input("input second number"))
count=0

for c in range(n1,n2+1):
    if c%2==0:
       print(f'[{c}]')

 