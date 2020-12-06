# Collections - Lists, practice (advanced)

# Create employees list
employees = ["Adam", "John" , "Greg" , "Danna", "Ashly"]
print("(1) - Print the list - " +str(employees))

# Length of the list
print("(2) - Length of the list is : " +str(len(employees)))

# Once 'John' left, 'Jack' took its place
employees[1] = "Jack"
print("(3) - Jack added instead of 'John'" +str(employees))

# New employee in the company - 'Mavrik', lets add it to index '3', without removing 'Danna'
employees.insert(3,"Mavrik")
print("(4) - Added 'Mavrik' to cell '3' : " +str(employees))

# Remove 'Mavrik' and add him to the end of the list, using 'append'
employees.remove("Mavrik")
print("(5-a) - Remove 'Mavrik' from the list : " +str(employees))

# Add 'Mavrik' to the end of the list
# employees.append("Mavrik")
employees.insert(5 , "Mavrik")
print("(5-b) - 'Mavrik' added to the end of the list :" +str(employees))

# Remove 'Mavrik' from the employees list
employees.pop(-1)
print("(6) - Remove 'Mavrik' from the list - " +str(employees))

# BONUS assignment - Sort the list by abc
employees.sort()
print("Sorted list : "+str(employees))
# All rights recerved to : https://www.programiz.com/





