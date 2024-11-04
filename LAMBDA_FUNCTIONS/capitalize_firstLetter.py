# #Use Lambda to Format Strings
# Given a list of names ["john", "mary", "susan"], use map() with a lambda function 
# to capitalize the first letter of each name.

names =["john", "mary", "susan"]
capitalized_names = list(map(lambda name:name.capitalize(),names))
print(capitalized_names)