n=int(input("enter a number of rows the triangle should have "))
s=n
a=""
b=""
for k in range(n+1):
    b+=" "
for i in range(n+1):
    print(b,end=a)
    a+="*"
    b=""
    s-=1
    for j in range(s,0,-1):
        b+=" "
    print()