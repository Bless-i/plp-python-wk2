# Step 1: Create an empty list called my_list
my_list = []  

# Step 2: Add elements 10, 20, 30, and 40 to the list
my_list.append(10)  # Adds 10 to the list
my_list.append(20)  # Adds 20 to the list
my_list.append(30)  # Adds 30 to the list
my_list.append(40)  # Adds 40 to the list

# Step 3: Insert the value 15 at the second position
my_list.insert(1, 15)  # Inserts 15 at index 1, which is the second position

# Step 4: Extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])  # Adds multiple elements at once to the end of the list

# Step 5: Remove the last element from my_list
my_list.pop()  # Removes the last element (70)

# Step 6: Sort my_list in ascending order
my_list.sort()  # Arranges elements in order from smallest to largest

# Step 7: Find and print the index of the value 30
index_of_30 = my_list.index(30)  # Finds the position of 30 in the list
print("Index of 30:", index_of_30)  # Displays the index of 30

# Print the final version of my_list to see the result
print("Final my_list:", my_list)
