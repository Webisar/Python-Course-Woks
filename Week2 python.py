# Here is an empty list of animals
animals_list = []

# Append elements
animals_list.append(10)
animals_list.append(20)
animals_list.append(30)
animals_list.append(40)

# Insertion of 15
animals_list.insert(1, 15)

# Extending the list with another list
animals_list.extend([50, 60, 70])

# Removing the last element from the list
animals_list.pop()

# Sorting the list in ascending order
animals_list.sort()

# Find and print the index of the value 30
index_of_30 = animals_list.index(30)
print("Index of 30:", index_of_30)
