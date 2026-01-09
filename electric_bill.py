un=int(input("number of units used "))

if un<=50:
    print("price of units used in rupees=",un*2.6+25)
elif un<=100:
    print("price of units used in rupees=",un*3.25+35)
elif un<=200:
    print("price of units used in rupees=",un*5.26+45)
elif un>200:
    print("price of units used in rupees=",un*8.45+75)