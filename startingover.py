print("hello we are starting over again with python")

while True:
    name=input("What's your name:")
    if name.isalpha():
        print("welcome",name)
        break
    else:
        print("you can only input name here")
while True:
    number=input("how old are you?")
    
    try:
        age=int(number)
        if age >= 18:
            print("you're eligible")
            break
        else:
            print("you're not eligible")
    except ValueError:
        print("your age should be a digit:")
        print("try again")