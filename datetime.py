import time



def new():
    file_name= input("enter file name:")
    content=input("what do you wish to be in this file? :")
    decision=input("do you want to create a file? (y/n): ")
    if decision.lower() == 'y':
        file_name = open(file_name, "w")
        file_name.write(content)
        file_name.close()

new()