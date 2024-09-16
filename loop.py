# Create a function* that takes an array, an index, and a value as parameters. Inside the function, use the insert method to insert the value at the specified index in the array. Return the modified array.
my_list:list = [1, 2, 3, 4]
def next(arr, index, value):
    my_list.insert (index, value)
    return arr
result = next (my_list, 2, 99)
print(result)

# Implement a simple shopping cart program* using an array. Create functions to add items, remove items, and update quantities using array methods. Print the cart's contents after each operation.
cart:list = ["eggs, oil, bread, honey, milk"]
item:str = ("salt")
def shopping (cart:str, item:str):
    cart.append ("item")
print (f"{item} added to the {cart}")

def shopping (cart:str, item:str):
    cart.pop (1)
print (f"oil removed from {cart}")

def shopping (cart:str, item:str):
    cart[3] = ("sugar")
print ("cart has been updated")

# Write a program* that uses a while loop to print the first 25 integers.
num:int = 1
while num <= 25:
    print(num)
    num += 1
    
# Write a program* that uses a while loop to print the first 10 even numbers.
for number in range (2, 21, 2):
    print (number)
    
# Create a function* that takes a positive integer as a parameter and uses a while loop to calculate and return the factorial of that number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(20)
print(result)

# Write a program* that has an array of numbers; if the number is negative, it should remove the negative number from the array.       
nums = [-1, -4, 7, -8, 9, -2]
i = 0
while i < len(nums):
    if nums[i] < 0:
        nums.remove(nums[i])
    else:
        i += 1
print(nums)
# Create a function* that takes an array of numbers as a parameter. Use a while loop to calculate and return the sum of all the numbers in the array.
numbers = [1, 2, 3, 4, 5]
def sum_of_numbers(nums):
    i = 0  
    total_sum = 0  
    while i < len(nums):
        total_sum += nums[i]  
        i += 1  
    return total_sum  
result = sum_of_numbers(numbers)
print(f"The sum of the array is: {result}")

 # Write a program* to remove all the odd numbers from an array.
nums = [1, 4, 5, 10, 13, 2]
i = 0
while i < len(nums):
    if nums[i] % 2 != 0:
        nums.remove(nums[i])
    else:
        i += 1
print(nums)

# Implement a program* that takes a list of temperatures in Celsius as input from the user. Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and store the converted temperatures in an array. Use a while loop to perform the conversion for each temperature.
def convert_celsius_to_fahrenheit(celsius_list):
    fahrenheit_list = []  
    i = 0  
    while i < len(celsius_list):
        fahrenheit = (celsius_list[i] * 9/5) + 32
        fahrenheit_list.append(fahrenheit)
        i += 1
    return fahrenheit_list
celsius_temperatures = [-10, 0, 10, 20, 30]
result = convert_celsius_to_fahrenheit(celsius_temperatures)
print(result)