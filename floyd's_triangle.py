r=int(input("enter a number of rows the triangle should have "))
n=1

print("Floyd's triangle")
for i in range(1,r+1):
    for k in range(1,i+1):
        print(n,end=" ")
        n=n+1
    print()