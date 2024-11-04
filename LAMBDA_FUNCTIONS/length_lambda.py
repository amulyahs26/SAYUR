# Find Words Longer than 5 Characters
# Use filter() and a lambda function to find all words longer than 5 characters 
# from the list:["hello", "world", "python", "lambda", "functional"].

list_words=["hello", "world", "python", "lambda", "functional"]
longer_words=list(filter(lambda word:len(word)>5,list_words))
print(longer_words)