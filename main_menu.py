# checks if the number entered is between 1-5 or 1,3 or whatever has been stated
# check int function
def check_int(question, error, low, high):
    valid = False

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

# main menu
print("1. Check your virtual pet's weight\n"
      "2. feed your virtual pet\n"
      "3. Exercise your virtual pet\n"
      "4. Help\n"
      "5. Exit virtual pet\n")
# checks if the number entered is between 1-5
menu_choice = check_int("Enter the number of your choice:", "Please choose a number between 1 and 5.", 1, 5)
print()


