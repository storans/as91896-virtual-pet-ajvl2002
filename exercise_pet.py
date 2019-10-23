#exercise_values = {"hop": 0.2, "run": 0.3, "walk": 0.1}

def show_food():
    number = 1
    for food in food_values:
        print("{}.  {}".format(number, food.title()))
        number += 1

def chosen_food():
    food_menu = []
    total_weight = 0
    total_food = 0
    start_weight = 1.5
    print("Please choose an option from the following foods:")

#    number = 1
#    for food in food_values:
#        print("{}.  {}".format(number, food.title()))
#        number += 1
#        food_menu.append(food)
#food_choice = int(input("Please choose an option from the list above by typing the number: "))

# main_menu
food_values = {"carrot": 0.2, "broccoli": 0.2, "kale": 0.1, "grass": 0.3}
print("1. Check your virtual pet's weight\n"
      "2. feed your virtual pet\n"
      "3. Exercise your virtual pet\n"
      "4. Help\n"
      "5. Exit virtual pet\n")
menu_choice = int(input("Enter your choice:"))

# print("test {}".format(menu_choice))

if menu_choice == 1:
    show_food()
    print("pet name's weight is ")

