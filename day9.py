#break
#allows a program execution to exit a loop once a given condition is trigered.
user_input=input("enter a sentence: ")
for i in (range(len(user_input))):
    if user_input[i]=="a":
        print("a found a index",i)
        break

user_input1=input("enter another sentence: ")
for i in user_input1:
    if i==" ":
        break 
    print(i,end="")
    
     
        

