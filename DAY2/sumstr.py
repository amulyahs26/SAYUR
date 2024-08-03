'''Find the sum and average of numbers present in a string
Eg. IAD23GY*78
SUM = 2 + 3 + 7+8 = 20'''

word = input("Enter the string input: ")

def sum_and_average_of_digits(word):
    sum_of_digits = 0
    digit_count = 0

    for i in word:
        if i.isdigit():
            sum_of_digits += int(i)
            digit_count += 1

    if digit_count > 0:
        average_of_digits = sum_of_digits / digit_count
        return sum_of_digits, average_of_digits
    else:
        return "String has no digits to sum or average"


result = sum_and_average_of_digits(word)
if isinstance(result, tuple):
    sum_of_digits, average_of_digits = result
    print(f"SUM = {sum_of_digits}")
    print(f"AVERAGE = {average_of_digits}")
else:
    print(result)
