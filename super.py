# check if person is eligible for superannuation

# age is a constant because it's not changed in the program
SUPER_AGE = 65

# a loop to allow testing of different values
keep_going = ""
while keep_going == "":
    age = int(input("What is your age?:"))
    # must be greater than or equal to 65
    if age >= SUPER_AGE:
        print("You are old enough to get super")

    else:
        print("You can not get super")

