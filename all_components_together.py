def formatter(character, output):
    print(character * (len(output) + 4))
    print("{} {} {}".format(character, output, character))
    print(character * (len(output) + 4))

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



# feed pet
def formatter(character, output):
    print(character * (len(output) + 4))
    print("{} {} {}".format(character, output, character))
    print(character * (len(output) + 4))

def show_items(dictionary_name):
    number = 1
    for item in dictionary_name:
        print("{}.  {}".format(number, item.title()))
        number += 1

def choose_item(list_name):
    choice = check_int("Please choose an option from the foods above:", "Please choose a number between 1 and 5.", 1, 5)
    print()
    choice = choice - 1
    chosen_item = list_name[choice][1]
    return chosen_item

# weight
def weight_calc(current_weight, choice, list_name):
    total_weight = current_weight + choice
    return total_weight



# exercise pet
def show_items(dictionary_name):
    number = 1
    for item in dictionary_name:
        print("{}.  {}".format(number, item.title()))
        number += 1

def item_chosen(name_list):
    choice = check_int("Please choose an option from the following forms of exercise:", "Please choose a number between 1 and 3.", 1, 3)
    choice = choice - 1
    item_chosen = name_list[choice][1]
    return item_chosen


# weight
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

# tracking_on = True
# while tracking_on == True:
# while True:

formatter("*", "Virtual pet")

name = input("Please choose a name for your virtual pet Rabbit:")
try:
    val = int, float(name)
    print("Please choose another name for your virtual pet rabbit.")
except ValueError:
   print("{} is a great name for your virtual pet rabbit!".format(name))


pet_alive = True
while pet_alive:
    # main_menu

    print()
    print("Main menu:")
    print("1. Check your virtual pet's weight\n"
          "2. feed your virtual pet\n"
          "3. Exercise your virtual pet\n"
          "4. Help\n"
          "5. Exit virtual pet\n")
    menu_choice = check_int("Enter the number of your choice:", "Please choose a number between 1 and 5.", 1, 5)
    print()

    # Check virtual pets weight
    if menu_choice == 1:
        if weight == 1.5:
            print("Please feed or exercise your pet")
        else:
            print("Your pet weighs {}kg".format(weight))

    # feed pet
    if menu_choice == 2:
        show_items(FOOD_DICTIONARY)
        food = choose_item(FOOD_LIST)
        weight = weight_calc(weight, food, FOOD_LIST)
        print("{} weighs {}kgs".format(name, weight))
        if pet_alive == True:
            print("Now {} needs to do some exercise! Please use the main menu and exercise {}.".format(name, name))
        elif weight >= 2 or weight <= 1:
            pet_alive = False
            print("We are sorry to inform you but your pet has died because it had to much to eat and not enough exercise")

    # exercise pet
    if menu_choice == 3:
        show_items(EXERCISE_DICTIONARY)
        exercise = item_chosen(EXERCISE_LIST)
        weight = calc_weight(weight, exercise, EXERCISE_LIST)
        print("Your pet weighs {}kgs".format(weight))

    # help
    if menu_choice == 4:
        print("1. About Virtual Pet\n"
              "2. How to use Virtual Pet\n")
        help_choice = check_int("Please enter the number of the option you wish to do:", "Please choose a number between 1 and 5.", 1, 5)
        print()

        if help_choice == 1:
            print("This virtual pet program is great if you are allergic to animals or are unable to keep a pet because you are renting etc...")
            print()


        if help_choice == 2:
            print("On Virtual Pet you can choose a name for your pet Rabbit and can look after it just like a real pet!")
            print("The game requires you to feed your pet rabbit and exercise it to make sure it doesn't get overweight or underweight.")
            print("If the rabbit's weight gets below or equal to 1kg or above or equal to 2kg then the rabbit will die.")
            print()


    # exit
    if menu_choice == 5:
        tracking_on = False
        print("Thanks for playing!")
        break

