#i'm making something like "diary" or a private log book
#Has a name first ,then password and then enter message of the day
def user_validation():
    first_name=input("Enter first name: ")
    last_name=input("enter last name: ")
    
    password=input("enter password: ")

    while len(password) < 6:
            password= input("password too short.Enter new password: ")

    print(f"welcome {first_name} {last_name}")

user_validation()



    

    