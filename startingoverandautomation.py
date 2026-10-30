def name():
    
 while True:
    name=input("welcome!,Enter your first name:")
 
    if name.isalpha():
         print("Hello",name,"welcome")
         break
    else:
         print("name is invalid try again")
    
name()

while True:
    number=(input("how old are you?"))
   
    try:
        age=int(number)
        if age >= 18:
            print("you're elligible")
            break
    except ValueError:
        print("your age should be a number")
        print("try again")
        

def file_maker():
   print("let's make a file")
   
   while True:
    file_name=input("enter filename(no spaces):")
    if file_name != " ":
        print("file name is valid")
        break
    else:
        print("file name is invalid")
        print("try again")
        
   while True:
        try:
            content=input("what do you want to be within this file:")
            if content !=" " :
                print("file content valid")
                break
        except ValueError:
                print("file content is invalid")
                print("try again")
                
                
   while True:
        confirming=input("create file(enter yes or no)")
      
            
        if confirming.lower()=="yes":
                new_file=open(file_name,"w")
                new_file.write(content)
                new_file.close()
                break
        elif confirming.lower()=="no":
                print("so you just wasted your time")
                break
        else:
                print("invalid input.either a yes or no needed")
                print("try again")
file_maker()
