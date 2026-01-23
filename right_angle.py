n=int(input("enter a number of rows the triangle should have "))

for i in range(n):
    for k in range(i+1):
        print("*",end="")
    print()