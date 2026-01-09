pick=str(input("pick a ride:\n bike or car "))

if pick=="bike":
    bike_type=str(input("you have picked bike select a type of bike:\ne-bike or pedal bike "))
    if bike_type=="e-bike":
        print("you have picked a e-bike")
    elif bike_type=="pedal bike":
        print("you have picked pedal bike")
    else:
        print("invaid selection please restart the program to try again")
elif pick=="car":
    car_type=str(input("you have picked car select a type of car:\nmazda or bmw "))
    if car_type=="mazda":
        print("you have picked mazda")
    elif car_type=="bmw":
        print("you have picked bmw")
    else:
        print("invaid selection please restart the program to try again")
else:
    print("invaid selection please restart the program to try again")