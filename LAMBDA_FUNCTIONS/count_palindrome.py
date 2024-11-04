#Count Palindromes:Use filter() to find how many palindromes are in the list:
# ["level", "world", "madam", "python", "radar"]

palindrome_list = ["level", "world", "madam", "python", "radar"]
palindromes = list(filter(lambda word: word == word[::-1], palindrome_list))
count = len(palindromes)

print("Number of palindromes:", count)