#formatted strings
f_temp=32
print(f'the temperature is {f_temp} degrees celcius')
#the value of the literal string is inserted
#improves readability
sun=27000
print(f'the temperature of the sun is {(sun-32)/1.8:,.1f}')
print(f'the temperature of the sun is {(sun-32)/1.8:,.1e}')
print(f'the temperature of the sun is {(sun-32)/1.8:,.1%}')


#formatting numbers
#d
#default decimal integer
print(f"{123456789:d}")
#decimal integer with comma seperators
print(f"{123456789:,d}")
#decimal integer,atleast 10 character wide
print(f"{123456789:10d}")
#decimalinteger,atleast 10 characters wide,with leading zeros
print(f"{123456789:010d}")
#f
import math
#default fixed point
print(f'{math.pi:f}')
#user fixed point
print(f'{math.pi:.9f}')
#user fixed point with character width
print(f'{math.pi:10.6f}')
#user fixed point with character width and leading zeros
print(f'{math.pi:0010.6f}')
month="M"
day="D"
year="Y"
print(f"{month}/{day}/{year}")

#madlid, try it
name=input("enter a name:")
noun=input("enter a noun:")
adjactive=input("enter an adjactive:")
verb=input("verb ending in-ing:")
print(f'{name} is a {adjactive} {noun} that likes {verb} ')

#try it wage calculator
hour_in=int(input("starting hour(9-5):"))
minute_in=int(input("starting minute(1-59):"))
hour_out=int(input("stopping hour(9-5):"))
minute_out=int(input("stopping minute9(1-59):"))
hourly_wage=float(input("hourly wage:"))

hours_used=hour_out-hour_in
minutes_used=minute_out-minute_in
minutes_to_hours=minutes_used/60
print(f"worked {hour_in}:{minute_in} to {hour_out}:{minute_out}")
total_hours=hours_used+minutes_to_hours
print(f'{total_hours}')
payment=hourly_wage*total_hours
print(f'{payment}')


#property of objects
a=1
b=2
c=b
b=a
a=c
print(c)
print(b)
print(a)

#tryit Different types
name="chocolate"
length=len(name)
price=1.99
lower=min(length,price)
product=name
name=name*2
#list
new_list=[3,4,5]
print("3rd number",new_list[2])

#try it list basics
list=[2,23,39,6,-5]
list[2]=35
print(len(list),list[2])
#tuple
first_tuple=(1,"eye",2.4)
print(f"first_tuple:{first_tuple}")
print(first_tuple[1])

#creating a tuple with user input
a=input("enter a:")
b=input("enter b:")
c=input("enter c:")
my_data=(a,b,c)
print(f"my data={my_data}")
#decisions
#boolean, 1s and 0s
#bool() converts a value to a boolean value
#TRUE:any non-zero number ,any non-empty string
#false:0,empty string
bool(input())
#comparison operators
#equal to:==
#not equal to:!=
#greater than:>
#less than:<
#greater than or equal to:>=
#less than or equal to:<=
day=input("day of the week:")
in_love=(day=="friday")
print(in_love)

#try it Even numbers
number=int(input("number"))
even=number%2==0
print(f'{number} is even?{even}')
#if-else statement
#if statement defines actions to be performed when a condition is true
#else statement defines an action to be performed when a codition is false
