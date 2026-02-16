#nested decision
#meal orders
menu_choice=input("lunch or dinner")
if menu_choice=="lunch":

    print("lunch options\n"
       "1:ceasar salad\n"
    "2:Spicy chicken wrap \n"
    "3:Butternut squash soup")
    meal_choice=int(input("choose your lunch meal:"))
    if meal_choice==1:
       print("your order:ceaser salad")
    elif meal_choice==2:
       print("your choice:spicy chicken wrap")
    elif meal_choice==3:
       print("your choice:Butternut squash soup")
    else:
       print("out of bounds")

elif menu_choice =="dinner":
    print("1:Baked Salmon\n"
       "2:Turkey burger\n"
       "3:Mushroom risotto")
    meal_choice_dinner=int(input("choose your dinner meal:"))
    if meal_choice_dinner==1:
        print("your order:Baked Salmon")
    elif meal_choice_dinner==2:
       print("your choice:Turkey burger")
    elif meal_choice_dinner==3:
       print("your choice:Mushroom risotto")
    else:
       print("out of bounds")
else:
   print("choice out of bounds")

#conditional expression
#simplified,single-line version of an if-else statement.
#expression_if_true if condition else expression_if_false

#tryit
#ping values
ping_values=int(input("ente pinf:"))
ping_report= "ping is low to average" if ping_values< 150 else "ping is too high"
print(ping_report)

#loops
# a loop is a codeblock that runs a set of statements while a condition is true.
#it is used for performing a repeating task.
#whileloop