#i'm making something like "diary" or a private log book
#Has a name first ,then password and then enter message of the day
def user_validation():
    first_name=input("Enter first name: ")
    last_name=input("enter last name: ")
    
    password=input("enter password: ")

    while len(password) < 6:
            password= input("password too short.Enter new password:")

    print(" \n")    
    print(f"welcome {first_name} {last_name}")
    print(" ")

user_validation()
    


import datetime
def logday():
    year = int(input('Enter a year: '))
    month = int(input('Enter a month :'))
    day = int(input('Enter a day: '))
    date1 = datetime.date(year, month, day)


logday()

def logmessaage():
     mesage=input("what happened today? : ")

logmessaage()


def want_to_see():
    print("open 'diary'?")
    name=input("what's your name :")
    password_1=input("enter password: ")
   



    

    