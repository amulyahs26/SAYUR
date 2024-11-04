# #Filter Even Length Words from a Sentence
# Given a string:"This is a simple sentence with some even length words"Use filter() 
# and a lambda function to extract only the words with even lengths.

string = "This is a simple sentence with some even length words"
words = string.split()
even_length_words = list(filter(lambda word: len(word) % 2 == 0, words))
print(even_length_words)