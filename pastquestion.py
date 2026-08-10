def collect_rainfall():
    bootstrap = "Enter rainfall amount for"
    day_one = float(input(f"{bootstrap} day one: "))
    return day_one

result=collect_rainfall()
print(f"Recorded amount: {result}")