# prints list of food to feed to pet
def show_food():
    #total_weight = 0
    total_food = 0
    start_weight = 1.5
    print("Please choose an option from the following foods:")

    number = 1
    for food in food_values:
        print("{}.  {}".format(number, food.title()))
        number += 1
        food_values(food)
    food_choice = int(input("Please choose an option from the list above by typing the number: "))
    #print(food_choice)

# weight
#chosen_food = food_choice[choice - 1]
#print("The {} will be added to the rabbits weight".format(chosen_food.title()))
#total_weight = start_weight + food_values[chosen_food]
#return chosen_food, total_weight;

# main menu
food_values = {"carrot": 0.2, "broccoli": 0.2, "kale": 0.1, "grass": 0.3}
print("1. Check your virtual pet's weight\n"
      "2. feed your virtual pet\n"
      "3. Exercise your virtual pet\n"
      "4. Help\n"
      "5. Exit virtual pet\n")
menu_choice = int(input("Enter your choice:"))

if menu_choice == 1:
    show_food()
    print("pet name's weight is ")




# prints list of food to feed to pet
#def show_food():
   #total_weight = 0
#    food_values = {"carrot": 0.2, "broccoli": 0.2, "kale": 0.1, "grass": 0.3}
#    total_food = 0
#    start_weight = 1.5
#    print("Please choose an option from the following foods:")


#    number = 1
 #   for food in food_values:
 #       print("{}.  {}".format(number, food.title()))
 #       number += 1
#        food_values.append(food)
 #   food_choice = int(input("Please choose an option from the list above by typing the number: "))
 #   print(food_choice)

# weight
#chosen_food = food_choice[choice - 1]
#print("The {} will be added to the rabbits weight".format(chosen_food.title()))
#total_weight = start_weight + food_values[chosen_food]
#return chosen_food, total_weight;


# main menu
#print("1. Check your virtual pet's weight\n"
#      "2. feed your virtual pet\n"
#      "3. Exercise your virtual pet\n"
#      "4. Help\n"
#      "5. Exit virtual pet\n")
#menu_choice = int(input("Enter your choice:"))


#if menu_choice == 1:
#    #show_food()
#    print("pet name's weight is {}".format(total_weight))
