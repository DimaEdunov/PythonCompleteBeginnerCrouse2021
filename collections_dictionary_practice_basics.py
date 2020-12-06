# Collections Dictionary practice (basics)

# Create a dictionary about Alex
alex = {'Age' : 32 , 'Married' : 'Yes' ,'Kids' : 3}
print("(1) - This is Alex's dictionary : " +str(alex))

# Extract values of the dictionary into variables
age = alex['Age']
marriage_status = alex['Married']
number_of_kids = alex['Kids']

print("(2) - Print of 'age' value " +str(age))
print("(2) - Print of 'marriage_status' value : " +marriage_status)
print("(2) - Print of 'number_of_kids' value : " +str(number_of_kids))

# (3) BONUS - Find a way to change dictionary value (Online)

# Change of 'Age' cell value, from 32 to 33
age_helper_dictionary = {'Age' : 33}
alex.update(age_helper_dictionary)
print("(4) - Update of a dictionary value, change of age : " +str(alex))

# Alex has a new kid joining the family
kids_helper_dictionary = {'Kids': 4}
alex.update(kids_helper_dictionary)
print("(5) - Update of a dictionary value, chage of number of kids : " +str(alex))

# Print the keys of 'alex' dictionary
print("(6) - print all keys of 'alex' dictionary : " +str(alex.keys()))

# Print the value of 'alex' dictionary
print("(7) - print all values of 'alex' dictionary : " +str(alex.values()))


