# Check if the number is Even or Odd.
num:int = (6)
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
    
# Check if the number is Positive, Negative, or Zero
if num > 0:
    print("the number is positive")
elif num < 0:
    print("the number is negative")
else:
    print("the number is zero")

# Check whether it is divisible by both 2 and 3 or anyone of them or not divisible by both
if num % 2 == 0 and num % 3 == 0:
    print("the number is divisible by both")
elif num % 2 == 0:
    print("the number is divisible by 2")
elif num % 3 == 0:
    print("the number is divisible by 3")
else:
    print("the number is not divisible by both")

# Determine voter eligibility based on age and nationality
age: int= (23)
nationality: str = ("Pakistani".lower())
if age >= 18:
    if nationality == "pakistani":
        print("You are eligible to vote.")
    else:
        print("Please obtain a valid ID to vote.")

# Write a program that takes the age of a person as input and determines whether they are a child (0-12 years), teenager (13-19 years), adult (20-59 years), or senior citizen (60 years and above)
Age:int = 23
if 0 < Age <= 13:
    print("you are a child")
elif 13 <= Age <= 19:
    print("you are a teenager")
elif 20 <= Age <= 59:
    print("you are a adult")
else:
    print("you are a senior citizen")

# Print the number of days in that month
month:int = 9
if 8 < month < 12:
    print("30 days")
else:
    print("31 days")

# Check if a year is a leap year or not.
year:int = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("its a leap year")
else:
    print("its not a leap year")

        



