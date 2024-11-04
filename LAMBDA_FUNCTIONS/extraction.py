#Extract Names Starting with a Given Letter
# Given a list of names ["Alice", "Bob", "Charlie", "David", "Eve"], use filter() 
# with a lambda function to extract names starting with the letter 'A' or 'C'.

names = ["Alice", "Bob", "Charlie", "David", "Eve"]
names_AorC=list(filter(lambda names:names.startswith("A") or names.startswith("C"),names))
print(names_AorC)