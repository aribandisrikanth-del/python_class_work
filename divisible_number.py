numerator=int(input("enter a number/numerator: "))
denominator=int(input("enter a number/denominator: "))

if numerator%denominator==0:
    print(str(numerator),"is divisible by",str(denominator))
else:
    print(str(numerator),"is not divisible by",str(denominator))