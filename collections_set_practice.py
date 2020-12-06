# Data collections - Set, practice

# 1 - Create a new 'set' collection of 'drinks'
drinks = {"Cola", "Sprite", "Beer", "Water", "Soda"}
print("(1) - 'Set' collection printout : " +str(drinks))

# 2 - Add additional cell with 'Soda' value
drinks.add("Soda")
print("(2) - Printing 'drinks' after adding additional 'Soda' cell : " +str(drinks))

# 3 - Delete 'Soda' out of the 'set' collection
drinks.remove("Soda")
print("(3) - print 'drinks' after deleting 'Soda' cell : " +str(drinks))

# 4 - Copy the 'drinks' into a new 'set' collection
drinks_2 = drinks.copy()
print("(4) - print 'drinks_2 set collection : " +str(drinks_2))

# 5 - BONUS : Print the length of the collection
print("(5) - The length of the collection 'drinks' is : " +str(len(drinks)))