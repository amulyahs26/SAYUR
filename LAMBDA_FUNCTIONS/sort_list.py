#Sort a List of Tuples by the Second Value
# Given a list of tuples representing students and their scores:
# [("Alice", 85), ("Bob", 75), ("Charlie", 95)]
# Use the sorted() function with a lambda to sort the tuples based on the scores (second element).

students=[("Alice", 85), ("Bob", 75), ("Charlie", 95)]
sorted_students=sorted(students,key=lambda items:items[1])
print(sorted_students)