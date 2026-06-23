def print_phone_num(): 
  print("Phone: (", 864, ")", 555, "-", 199) 
print("User info:") 
print_phone_num() 
#FUNCTION=  REUSABLE BLOCK OF CODE
def concession():
  print("Food/Drink Options:") 
  print("Popcorn: $8-10 ")
  print("Candy: $3-5")
  print("Soft drink: $5-7")
concession()

def extra_lot(): 
   """Output extra parking lot info.""" 
   print("Take the second right to park.") 
 
def park_greet(): 
   """Output greeting.""" 
   print("Welcome. Open sunrise to sunset.") 
 
car_count = 1 
park_greet() 
if car_count > 50: 
   extra_lot() 
