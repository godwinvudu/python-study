def collect_rainfall():
    bootstrap = "Enter rainfall amount for"
    day_one = float(input(f"{bootstrap} day one: "))

    day_2=float(input(f"{bootstrap} day two: "))

    day_3=float(input(f"{bootstrap} day three: "))

    day_4=float(input(f"{bootstrap} day four: "))

    day_5=float(input(f"{bootstrap} day five: "))

    day_6=float(input(f"{bootstrap} day six: "))

    day_6=float(input(f"{bootstrap} day seven: "))
    
result=collect_rainfall()
print(f"Recorded amount: {result}")