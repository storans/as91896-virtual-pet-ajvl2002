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

# puts stars or exclamation points around words if the formatter is used
def formatter(character, output):
    print(character * (len(output) + 4))
    print("{} {} {}".format(character, output, character))
    print(character * (len(output) + 4))

# show items function
def show_items(dictionary_name):
    number = 1
    for item in dictionary_name:
        print("{}.  {}".format(number, item.title()))
        number += 1

# choose item function
def choose_item(list_name):
    choice = check_int("Please choose an option from the following forms of exercise:", "Please choose a number between 1 and 3.", 1, 3)
    choice = choice - 1
    chosen_item = list_name[choice][1]
    return chosen_item

# weight
# calculates the pets weight function
def weight_calc(current_weight, choice, list_name):
    total_weight = current_weight - choice
    return total_weight



# Main Routine
start_weight = 1.5
EXERCISE_DICTIONARY = {"hop": 0.2, "run": 0.3, "walk": 0.1}
EXERCISE_LIST = [["hop", 0.2], ["run", 0.3], ["walk", 0.1]]

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
menu_choice = check_int("Please enter the number of the option you wish to do:", "Please choose a number between 1 and 5.", 1, 5)
print()

# if menu choice equals 3 do this...
if menu_choice == 3:
    show_items(EXERCISE_DICTIONARY)
    exercise = choose_item(EXERCISE_LIST)
    weight = weight_calc(start_weight, exercise, EXERCISE_LIST)
    print("Your pet weighs {}kgs".format(weight))

