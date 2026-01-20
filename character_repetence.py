s=input("plese enter your own word: ")
c=input("please enter a character to check how many times has been repeated in the given word: ")

i=0
co=0
while(i<len(s)):
    if(s[i]==c):
        co=co+1
    i=i+1

print("the total number of times",c,"was repeated in",s,"is",co)