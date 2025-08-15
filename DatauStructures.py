
# This is a file to submit the week 2 assignment on Data structures


#Create an empty list
my_list =[]

# Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("my_list:", my_list)

# Insert the value 15 at the second position in the list.
my_list.insert(1, 15)

print("After inserting 15 at second position:", my_list)

# Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])

print("After extending with [50, 60, 70]:", my_list)

# Remove the last element from my_list.
my_list.remove(my_list[-1])

print("After removing the last element:", my_list)

# Sort my_list in ascending order.
my_list.sort()

print("After sorting in ascending order:", my_list)

# Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)

print("Index of 30 in my_list:", index_of_30)

# That has been a tough week, but I have learned a lot about lists and their operations in Python.
