def sum(x, y):
    return x + y    
#call back functions

print(sum(2, 3))
#rock paper sciscors game

#ask user for name
def username():
    user_name=input("enter username:" )
    want_to_play=input(f"hey {user_name} ready to play rock ,paper,sciscors")
    while want_to_play:
        if want_to_play=="no" or "No":
            print("good bye then")
            break
        elif want_to_play=="yes" or "Yes":
            print("ok lets's do this")
        else:
          print("enter either a yes or no :")
       
    return username

def main():
    start_1=username


