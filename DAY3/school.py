'''Calcualte and print which standard the student is studying - Write a program to ask the user for his/her name
and print 'Hello', user's name. 
Ask what year they were born.
eg Hello Chitra, what year were you born?
get the year from the user. 
Calculate if the user is going to elementary school, middle school, highschool or college, based on users age. 
(hint - use if/elif)'''

from datetime import datetime,timedelta

# Get the current date
current_date = datetime.now().date()

# Get and validate user name
while True:
    name = input("Enter your name: ")
    if name.isalpha():
        break
    else:
        print("Please enter a valid name (letters only).")

# Get and validate birth year
while True:
    birth_year = int(input("Enter your birth year: "))
    current_year = current_date.year
    if birth_year >= current_year or birth_year < 1900:
        print("Please enter a valid year.")
    else:
        break

# Get and validate birth month
while True:
    birth_month = int(input("Enter your birth month (1-12): "))
    if birth_month < 1 or birth_month > 12:
        print("Please enter a valid month (1-12).")
    else:
        break

# Get and validate birth day
while True:
    birth_day = int(input("Enter your birth day: "))
    try:
        birth_date = datetime(birth_year, birth_month, birth_day).date()
        break
    except ValueError:
        print("Please enter a valid day for the given month and year.")

# Calculate the age
age_years = current_date.year - birth_date.year
age_months = current_date.month - birth_date.month
age_days = current_date.day - birth_date.day

# Adjust for negative months or days
if age_days < 0:
    age_months -= 1
    age_days += (current_date.replace(day=1) - timedelta(days=1)).day  # Get the last day of the previous month

if age_months < 0:
    age_years -= 1
    age_months += 12

print(f"Hello {name}!!! You are {age_years} years, {age_months} months, and {age_days} days old.")
if age_years<=10:
    print("You are studing to elementary school")
elif age_years<=15 and age_years>=10:
    print("You are studing to middle school")
else:
    print("You are going to high school or college")

    
