SUPER_AGE = 65

keep_going = ""
while keep_going == "":
    age = int(input("What is your age?:"))
    if age >= SUPER_AGE:
        print("You are old enough to get super")

    else:
        print("You can not get super")

