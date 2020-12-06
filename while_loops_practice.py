# While loops practice

# PART A
ages = [5, 6, 24, 32, 21, 70]

counter = 0
while ages[counter] < 30:

    print("Part A - The ages is : " +str(ages[counter]))
    counter+=1

print("Part A - The value that caused the loop to stop : " +str(ages[counter]))

print("\n")


# PART B
counter = 0

while ages[counter] < 30:
    if ages[counter] > 20 :
        print("Part B - Print the value that stopped the loop : " +str(ages[counter]))
        break

    counter +=1

print("\n")

# PART C
counter = 0
while ages[counter] < 70:
    ages[counter] = ages[counter] + 2
    print("Part C - Cell's new value is : " +str(ages[counter]))

    counter +=1

else:
    print("Part C - I'm inside 'else' because the number : " +str(ages[counter]))
