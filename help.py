# checks if the number entered is between 1-5 or 1,3 or whatever has been stated
# check int function
def check_int(question, error, low, high):
    valid = False

    # while loop
    while valid == False:
        number = input("{}".format(question))
        try:
            number = int(number)
            if low <= number <= high:
                return number
            else:
                print(error)
        except ValueError:
            print(error)

tracking_on = True
# while loop
while tracking_on == True:
    while True:

        # main menu
        print("Main menu:")
        print("1. Check your virtual pet's weight\n"
              "2. feed your virtual pet\n"
              "3. Exercise your virtual pet\n"
              "4. Help\n"
              "5. Exit virtual pet\n")
        # checks if the number entered is between 1-5
        menu_choice = check_int("Enter the number of your choice:", "Please choose a number between 1 and 5.", 1, 5)
        print()

        # if menu choice equals 4 do this...
        if menu_choice == 4:
            print("1. About Virtual Pet\n"
              "2. How to use Virtual Pet\n")
        # checks if the number entered is between 1-2
        help_choice = check_int("Please enter the number of the option you wish to do:", "Please choose a number between 1 and 2.", 1, 2)
        print()

        # if help choice equals 1 do this...
        if help_choice == 1:
            print("This virtual pet program is great if you are allergic to animals or are unable to keep a pet because you are renting etc...")
            print()
            break

        # if help choice equals 2 do this...
        if help_choice == 2:
            print("On Virtual Pet you can choose a name for your pet Rabbit and can look after it just like a real pet!")
            print("The game requires you to feed your pet rabbit and exercise it to make sure it doesn't get overweight or underweight.")
            print("If the rabbit's weight gets below or equal to 1kg or above or equal to 2kg then the rabbit will die.")
            print()
            break
