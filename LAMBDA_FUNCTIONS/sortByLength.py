#Sort by Length:Sort the following list of strings based on their lengths:
# ["apple", "banana", "cherry", "date"]

fruits=["apple", "banana", "cherry", "date"]
sorted_fruits=sorted(fruits,key=lambda fruits:len(fruits))
print(sorted_fruits)