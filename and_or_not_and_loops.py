#python has logical operators
#and
#0r
#not
x=6
y=0
legal=(y==0 or x/1==6)
print(legal)
#loops
#while loops
#as long as a condition remains true,excutre the statements
def main():
    count=500
    message="i am"
    i=0
    while i< count:
        print(i,message)
        i+=1
#main()
 #i want to execute other commands above 
def check_if_prime(n):
  if n<=1:
    return False
  for i in range(2,int(n**0.5)+1):
     if n%i ==0:
        return False
  return True



def main():
    while True:
        user_input=input("enter a number or type exit(to exit code):")
        if user_input.lower()=="exit":
           print("good bye")
           break
           
        number=int(user_input)
    
        even = number % 2==0
        odd = number % 2!=0
        prime=check_if_prime(number)
        if even and prime:
           print(f"{number} is even and prime ")
           
        elif even:
            print(f"{number} is even")
        if odd and prime:
            print(f"{number} is odd and a prime ")
        elif odd:
            print(f"{number} is odd")
        
        
main()


    