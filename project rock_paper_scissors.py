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
#number of rounds
def rounds():
   
    while True:
        try:
            rounds_=int(input("how many rounds: "))
            print(" ")
            if rounds_<=0:
                    print("no negatives or zero rounds allowed")

            else:
                    print(f"alright, we are playing {rounds_} rounds")
            return rounds_
        except ValueError:
            print("invalid input!PLEASE ENTER A WHOLE NUMBER: ")

        
#machines choice
def machine_choice():
    from random import choice
    options=["rock","paper","scissors"]
    computer_pick=choice(options)


    return computer_pick
#asking for player move
def player_choice():
    while True:
        user_pick=input("type in your move: ").lower()
        if user_pick=="rock" or user_pick=="paper"or user_pick=="scissors":
         return user_pick
        else:
            print("invalid option!")
#game logic.
def game_logic():
    userpick=player_choice()
    computerpick=machine_choice()
    print(f"you chose {userpick}")
    print(f"machine chose {computerpick}")
    if userpick==computerpick:
        print("its a tie")
        return "tie"

    elif (userpick=="rock" and computerpick=="scissors")or\
         (userpick=="paper" and computerpick=="rock")or\
         (userpick=="scissors" and computerpick=="paper"):
        print("you win!")
        return "player"
    else:
        print(f"haha i win!")
        return "computer"
    


#if they want to play again
def again():
    while True:
        again_=input("wish to play again!:").lower()
        if again_=="yes":
            print("alright lets do this")
            return True
        elif again_=="no":
           print("goodbye for now.")
           exit()
        else:
            print("invalid input/ enter a yes or no.")

      
#execute everything
def main():
    start_1=username()
    while True:
        total_rounds=rounds()

        playerscore=0
        computerscore=0
        for round_num in range(total_rounds):
          print(f"\--Round{round_num +1}---")
          result=game_logic()

          if result == "player":
                 playerscore += 1
          elif result == "computer":
                computerscore += 1
        
        print(f"\n===Final score===")
        print(f"player score is {playerscore } | machine score is {computerscore}")
        ag = again()

main()


            

        

