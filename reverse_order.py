num=abs(int(input("pick a number to count its digits ")))
sum=0
temp=num

while temp>0:
    digit=temp%10
    sum+=((digit-digit)+1)
    temp//=10

print("number of digits =",sum)