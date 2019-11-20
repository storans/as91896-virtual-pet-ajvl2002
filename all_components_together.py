# Final version
# This is a virtual pet program that allows you to have a virtual pet rabbit and feed and exercise it.
# puts stars or exclamation points around words if the formatter is used
def formatter(character, output):
    print(character * (len(output) + 8))
    print("{} {} {} {} {}".format(character, character, output, character, character))
    print(character * (len(output) + 8))

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


# feed pet
# show items function
def show_items(dictionary_name):
    number = 1
    # for item in dictionary
    for item in dictionary_name:
        # print number and food item
        print("{}.  {}".format(number, item.title()))
        number += 1

# choose item function
def choose_item(list_name):
    # checks if the number entered is between 1-5
    choice = check_int("Please choose an option from the foods above - enter a number between 1 and 5:", "Please choose a number between 1 and 5.", 1, 5)
    print()
    choice = choice - 1
    chosen_item = list_name[choice][1]
    return chosen_item

# weight
# calculates the pets weight function
def weight_calc(current_weight, choice, list_name):
    # the total weight is the current weight minus the value of the users choice
    total_weight = current_weight + choice
    return total_weight



# exercise pet
# show items function
def show_items(dictionary_name):
    number = 1
    # for item in dictionary
    for item in dictionary_name:
        # print number and food item
        print("{}.  {}".format(number, item.title()))
        number += 1

# choose item function
def item_chosen(name_list):
    # checks if the number entered is between 1-3
    choice = check_int("Please choose an option from the forms of exercise above - enter a number between 1 and 3:", "Please choose a number between 1 and 3.", 1, 3)
    print()
    choice = choice - 1
    item_chosen = name_list[choice][1]
    return item_chosen

# weight
# calculates the pets weight function
def calc_weight(total_weight, choice, name_list):
    # the total weight is the current weight minus the value of the users choice
    exercise_weight = total_weight - choice
    return exercise_weight




# Main Routine
# start/current weight
weight = 1.5
# maximum weight if the pet reaches this weight or above it dies
max_weight = 2
# minimum weight if the pet reaches this weight or below it dies
min_weight = 1
FOOD_DICTIONARY = {"carrot": 0.2, "broccoli": 0.2, "kale": 0.1, "grass": 0.3, "2 carrots": 0.4}
FOOD_LIST = [["carrot", 0.2], ["broccoli", 0.2], ["kale", 0.1], ["grass", 0.3], ["2 carrots", 0.4]]
EXERCISE_DICTIONARY = {"hop": 0.2, "run": 0.3, "walk": 0.1}
EXERCISE_LIST = [["hop", 0.2], ["run", 0.3], ["walk", 0.1]]


# puts stars (*) around Virtual Pet Rabbit
formatter("*", "Virtual Pet Rabbit")
# welcome the user to the game/program
print("Welcome to Virtual Pet Rabbit where you can have your very own virtual pet Rabbit!")
print()

# allows user to input a name for their pet
name = input("Please choose a name for your virtual pet Rabbit:")
# prints that the name is a great name
print("{} is a great name for your virtual pet Rabbit!".format(name))


# while the pet is alive do this...
pet_alive = True
# while loop
while pet_alive:

    print()
    # main menu
    formatter("*", "Main menu:")
    print("1. Check {}'s weight.\n"
          "2. Feed {}.\n"
          "3. Exercise {}.\n"
          "4. Help.\n"
          "5. Exit Virtual Pet Rabbit.\n".format(name, name, name, name))
    # user enters their choice and the check_int checks that the number is between 1 and 5
    menu_choice = check_int("Enter the number of your choice - a number between 1 and 5:", "Please choose a number between 1 and 5.", 1, 5)
    print()


    # Check virtual pets weight
    if menu_choice == 1:
        # if the weight is 1.5 the pet has not been fed or exercised so it tells the user to do that before using this
        if weight == 1.5:
            formatter("!", "{} weighs 1.5kg".format(name))
        else:
            formatter("!", "{} weighs {}kg.".format(name, weight))
            #print("{} weighs {}kg.".format(name, weight))


    # feed pet
    if menu_choice == 2:
        show_items(FOOD_DICTIONARY)
        food = choose_item(FOOD_LIST)
        weight = weight_calc(weight, food, FOOD_LIST)
        formatter("-", "{} weighs {}kg.".format(name, weight))
        # if the pet weighs 2kg or above or 1kg or less then the pet dies
        if weight >= 2 or weight <= 1:
            pet_alive = False
            formatter("=", "We are sorry to inform you but {} has died, because {} became an unhealthy weight because {} had had to much to eat and not enough exercise.".format(name, name, name))
        # if the pet is still alive do this...
        elif pet_alive == True:
            print("Now {} needs to do some exercise! Please use the main menu and exercise {}.".format(name, name))


    # exercise pet
    if menu_choice == 3:
        show_items(EXERCISE_DICTIONARY)
        exercise = item_chosen(EXERCISE_LIST)
        weight = calc_weight(weight, exercise, EXERCISE_LIST)
        formatter("-", "{} weighs {}kg.".format(name, weight))
        # if the pet weighs 2kg or above or 1kg or less then the pet dies
        if weight >= 2 or weight <= 1:
            pet_alive = False
            formatter("=", "We are sorry to inform you but {} has died, because {} exercised to much.".format(name, name, name))
        # if the pet is still alive do this...
        elif pet_alive == True:
            print("Now {} needs to be fed! Please use the main menu and feed {}.".format(name, name))


    # help
    if menu_choice == 4:
        print("1. About Virtual Pet Rabbit.\n"
              "2. How to use Virtual Pet Rabbit\n")
        # user enters their choice and the check_int checks that the number is between 1 and 2
        help_choice = check_int("Please enter the number of the option you wish to do - a number between 1 and 2:", "Please choose a number between 1 and 2.", 1, 2)
        print()

        # if user chooses 1
        if help_choice == 1:
            # will print...
            print("This virtual pet program is great if you are allergic to animals or are unable to keep a pet because you are renting or not allowed.")
            print()

        # if user chooses 2
        if help_choice == 2:
            # will print...
            print("On Virtual Pet Rabbit you can choose a name for your pet Rabbit and can look after it just like a real pet!")
            print("The game requires you to feed your pet Rabbit and exercise it to make sure it doesn't get overweight or underweight.")
            print("If the Rabbit's weight gets below or equal to 1kg or above or equal to 2kg then the rabbit will die.")
            print()


    # exit
    # if user chooses 5 the game will end
    if menu_choice == 5:
        tracking_on = False
        print("Thanks for playing!")
        break
