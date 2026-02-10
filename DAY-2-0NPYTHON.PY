animal="dog"
says="bark"
print(f"My {animal} says {says} {says} {says}")
#unicode
print(ord("!"))
#indexing
s="Godwin!"
print(s[3]+s[4]+s[1])
print("ha"*4)
#mixed data types
#float point errors
x=2.9
y=4
print(float(x*y))
print(round(float(x*y)))
print(round(6.6,2))

#dividing integers
#true division(/):converts number to float before dividing  
print(float(7/4))
#floor division(//):computes the number of times divided
print(float(19//2))
#modular operator(%):computes the remainder
print(float(9%3))
print(float(25%4))

#arrivaltime and triptime project
current_minute=(int(input("what minute is it" )))
current_hour=(int(input("what hour is it(1-12)")))
hour_to_minutes=(current_hour*60)
current_time=(current_minute+hour_to_minutes)
Trip_length=(int(input("what's the distance(5,000-50,000km)")))
average_plane_speed_in_kilometers_737=(850.0)
trip_time=(Trip_length/average_plane_speed_in_kilometers_737)
print(trip_time ,"is the flight time")
arrival_time_in_minutes=(int(trip_time+current_time))
arival_hour=int((arrival_time_in_minutes/24))
arrival_minute=(arrival_time_in_minutes%60)
print("arrival hour is",arival_hour)
print("arrival minute is",arrival_minute)

import math

import math

a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))

d = b*b - 4*a*c

x1 = (-b + math.sqrt(d)) / (2*a)
x2 = (-b - math.sqrt(d)) / (2*a)

print(x1)
print(x2)
