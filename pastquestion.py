def collect_rainfall():
    bootstrap = "Enter rainfall amount for"
    day_1 = float(input(f"{bootstrap} day one: "))

    day_2=float(input(f"{bootstrap} day two: "))

    day_3=float(input(f"{bootstrap} day three: "))

    day_4=float(input(f"{bootstrap} day four: "))

    day_5=float(input(f"{bootstrap} day five: "))

    day_6=float(input(f"{bootstrap} day six: "))

    day_7=float(input(f"{bootstrap} day seven: "))

    total=(day_1+day_2+day_3+day_4+day_5+day_6+day_7)
    return total
result=collect_rainfall()
print(f"Recorded amount: {result}")