# Collections tuple - practice

# 1 - Create a tuple of tech terms
technological_terms = ('python', 'pycharm IDE', 'tuple', 'collections', 'string')
print('(1) - This is the tuple collections : ' +str(technological_terms))

# 2 - Print a sentence using cell extraction : Regular & negative
#we are ninja developers. We write python code in pycharm IDE, and now practicing tuple collections topic, that contains string variables.

print("(2) - we are ninja developers. We write " +technological_terms[0] +" code in " +technological_terms[-4]
+", and now practicing " +technological_terms[2] +" collections topic, that contains " +technological_terms[-1] +" variables.")


# 3 - Insert 'float' and 'list' variables into the tuple
technological_terms_list = list(technological_terms)

technological_terms_list.append('float')
technological_terms_list.append('list')

technological_terms = tuple(technological_terms_list)
print("(3) - This is our new tuple with the added cells : " +str(technological_terms))


# 4 - Create a single cell tuple
single_cell_tuple = (1,)
print("(4) - Print the single cell tuple : " +str(single_cell_tuple))
print(type(single_cell_tuple))
