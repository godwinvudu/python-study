def sum(x, y):
    return x + y    
#call back functions

print(sum(2, 3))
#rock paper sciscors game

#ask user for name
def username():
    print("you are about to play a game of rock paper scissors!")
    user_name=input("enter username:" )
    while True:
        want_to_play=input(f"hey {user_name} ready to play rock ,paper,scissors :").lower()
    
        if want_to_play=="no" :
            print("good bye then")
            exit()

        elif want_to_play=="yes":
            print("ok lets's do this")
            break
        
        else:
          print("enter either a yes or no :")
       
    return user_name

def rounds():
   
    while True:
        rounds_=int(input("how many rounds: "))
        print(" ")
        if rounds_<=0:
            print("no negatives or zero rounds allowed")

        else:
            print(f"alright, we are playing {rounds_} rounds")
            break

    return rounds_

def machine_choice():
    from random import choice
    options=["rock","paper","scissors"]
    computer_pick=choice(options)


    return computer_pick

def player_choice():
    while True:
        user_pick=input("type in your move").lower()
    if user_pick=="rock" or user_pick=="paper"or user_pick=="scissors":
        return user_pick
    else:
        print("invalid option!")


    
def main():
    start_1=username()
    total_rounds=rounds()
    
main()


