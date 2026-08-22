# Program to demonstrate list operations

# Creating a list
my_list = [10, 20, 30, 40]
print("Original List:", my_list)

# I. Inserting an element
my_list.insert(2, 25)  
print("After Inserting 25 at index 2:", my_list)

# II. Removing an element
my_list.remove(20)  
print("After Removing 20:", my_list)

# III. Appending an element
my_list.append(50)  
print("After Appending 50:", my_list)

# IV. Displaying the length of the list
print("Length of the List:", len(my_list))

# V. Popping an element
popped = my_list.pop()  # Remove last element
print("Popped Element:", popped)
print("List after Pop:", my_list)

# VI. Clearing the list
my_list.clear()
print("List after Clearing:", my_list)