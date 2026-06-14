def main():
    name=input("what is your name? ")
    like=input("what do you like doing? ")
    print(name ,"likes" , like)

main()

def hello():
    
    import math
    #bmi calculator
    height=float(input("enter height(in metres):"))
    weight=float(input(("enter weight (in kilograms): ")))

    bmi=round(weight/(height)**2)
    print(f"your bmi is",bmi)

hello()
