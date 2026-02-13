#try it improvised division
numerator=(float(input("enter numerator:")))
denominator=(float(input("enter denominator:")))

if denominator==0:
    print("denominator should be above zero")
    new_denominator=float(input("enter new denominator:"))
    print(float(numerator/new_denominator))
else:
    print(numerator/denominator)

