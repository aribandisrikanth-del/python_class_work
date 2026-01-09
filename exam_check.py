c=str(input("what is your medical cause "))
at=int(input("what is your attendence "))

if c=="y":
    print("you are allowed")
else:
    if at>75:
        print("allowed")
    else:
        print("not allowed")