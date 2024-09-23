# Write a Python program to create a list of 5 numbers. Add an element to the list, remove one element, and find the maximum and minimum number in the list.
nums:list[int] = [1,2,3,4,5,6]
nums.insert(1,7)
nums.remove(5)
print (nums)
max_num = max(nums)
print (max_num)
min_num = min(nums)
print (min_num)

#Given a list of fruits: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango'], write a program to:
#Access the first, middle, and last element of the list.
fruits: list = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
first_element = fruits[0]
print (first_element)
last_element = fruits [-1]
print (last_element) 
middle_index = len (fruits) // 2
middle_element = fruits[middle_index]
print (middle_element)
#Change the second element to 'blueberry'.
fruits[1] = ("blueberry")
print (fruits)

#Write a program that takes a list of student names as input, sorts the names in alphabetical order, and prints the sorted list.
