# Given a string, find the first character which is a duplicate

# Eg. 
# input = "apple" -> output = 'p'
# input = probability, output = 'b'
# input = abchjhba, output = 'h'/

def first_duplicate_char(s):
    present = set()   
    for char in s:            #time complexity O(n)
        if char in present:
            return char
        present.add(char)
    
    return None
print(first_duplicate_char("apple")) 
print(first_duplicate_char("probability")) 
print(first_duplicate_char("abchjhba"))    
print(first_duplicate_char("abcdef")) 

    
