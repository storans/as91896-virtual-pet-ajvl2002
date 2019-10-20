name = input("Please choose a name for your virtual pet Rabbit:")
try:
    val = int, float(name)
    print("Please choose another name for your virtual pet rabbit.")
except ValueError:
   print("That is a great name for your virtual pet rabbit!")

print("{} is a healthy weight!".format(name))




