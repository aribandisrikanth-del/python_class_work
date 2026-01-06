a=int(input("enter a value: "))
b=int(input("enter a value: "))
c=int(input("enter a value: "))

avg_speed=((a+b+c)/3)
print("the average speed is",avg_speed,"\n")

if avg_speed<a and avg_speed<b and avg_speed<c:
    print("all of the bikes are faster than average speed")
elif avg_speed>a and avg_speed>b:
    print("all of the bikes are faster than average speed except the bike c going ",c,"kilometers per hour")
elif avg_speed<a and avg_speed<c:
    print("all of the bikes are faster than average speed except the bike b going ",b,"kilometers per hour")
elif avg_speed<c and avg_speed<b:
    print("all of the bikes are faster than average speed except the bike a going ",a,"kilometers per hour")
elif avg_speed<a:
    print("only bike a is going faster than average speed which is ",a,"kilometers per hour")
elif avg_speed<b:
    print("only bike b is going faster than average speed which is ",b,"kilometers per hour")
elif avg_speed<c:
    print("only bike c is going faster than average speed which is ",c,"kilometers per hour")