# check int function
# checks if the number entered is between 1-5
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

# formatter function
def formatter(character, output):
    print(character * (len(output) + 4))
    print("{} {} {}".format(character, output, character))
    print(character * (len(output) + 4))

# feed
def show_items(dictionary_name):
    number = 1
    for item in dictionary_name:
        print("{}.  {}".format(number, item.title()))
        number += 1

# choose item function
def choose_item(list_name):
    # checks if the number entered is between 1-5
    choice = check_int("Please choose an option from the foods above:", "Please choose a number between 1 and 5.", 1, 5)
    choice = choice - 1
    chosen_item = list_name[choice][1]
    return chosen_item

# weight calculator function
def weight_calc(current_weight, choice, list_name):
    total_weight = current_weight + choice
    return total_weight



# exercise

# show items function
def show_items(dictionary_name):
    number = 1
    for item in dictionary_name:
        print("{}.  {}".format(number, item.title()))
        number += 1

# choose item function
def item_chosen(name_list):
    # checks if the number entered is between 1-3
    choice = check_int("Please choose an option from the following forms of exercise:", "Please choose a number between 1 and 3.", 1, 3)
    choice = choice - 1
    item_chosen = name_list[choice][1]
    return item_chosen

# weight calculator function
def calc_weight(total_weight, choice, name_list):
    exercise_weight = total_weight - choice
    return exercise_weight


# Main Routine
weight = 1.5
max_weight = 2
min_weight = 1
FOOD_DICTIONARY = {"carrot": 0.3, "broccoli": 0.2, "kale": 0.1, "grass": 0.3, "2 carrots": 0.6}
FOOD_LIST = [["carrot", 0.3], ["broccoli", 0.2], ["kale", 0.1], ["grass", 0.3], ["2 carrots", 0.6]]
EXERCISE_DICTIONARY = {"hop": 0.2, "run": 0.3, "walk": 0.1}
EXERCISE_LIST = [["hop", 0.2], ["run", 0.3], ["walk", 0.1]]

pet_alive = True
# while pet alive do this...
while pet_alive:
    # main_menu
    formatter("*", "Virtual pet")
    print()
    print("Main menu:")
    print("1. Check your virtual pet's weight\n"
          "2. feed your virtual pet\n"
          "3. Exercise your virtual pet\n"
          "4. Help\n"
          "5. Exit virtual pet\n")
    # checks if the number entered is between 1-5
    menu_choice = check_int("Enter the number of your choice:", "Please choose a number between 1 and 5.", 1, 5)
    print()

    if menu_choice == 1:
        if weight == 1.5:
            formatter("!", "You need to feed or exercise your pet before you can check its weight")
            print()
        else:
            print("Your pet weighs {}kg".format(weight))


    if menu_choice == 2:
        show_items(FOOD_DICTIONARY)
        food = choose_item(FOOD_LIST)
        weight = weight_calc(weight, food, FOOD_LIST)
        print("Your pet weighs {}kgs".format(weight))
        # if the pet weighs 2kg or above or 1kg or less then the pet dies
        if weight >= 2 or weight <= 1:
            pet_alive = False
            print("We are sorry to inform you but your pet has died because it became an unhealthy weight")
            # if the pet is still alive do this...
        elif pet_alive == True:
            print("Now your pet needs to do some exercise! Please use the main menu and exercise your pet.")

    if menu_choice == 3:
        show_items(EXERCISE_DICTIONARY)
        exercise = item_chosen(EXERCISE_LIST)
        weight = calc_weight(weight, exercise, EXERCISE_LIST)
        print("Your pet weighs {}kgs".format(weight))
        # if the pet weighs 2kg or above or 1kg or less then the pet dies
        if weight >= 2 or weight <= 1:
            pet_alive = False
            print("We are sorry to inform you but your pet has died because it became an unhealthy weight")
            # if the pet is still alive do this...
        elif pet_alive == True:
            print("Now your pet needs to be fed! Please use the main menu to feed your pet.")

