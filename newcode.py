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
students:list = ["momna","amna","emaan","aswah","anveesha","rida"]
arranged_list = sorted(students)
print (arranged_list)

#Write a program that takes a list of integers and prints:
#The first 3 elements
#The last 2 elements
#The entire list in reverse order
nums1:list = [10,11,12,13,14,15]
print(nums1[:3])
print (nums1[-2:])
nums1.reverse ()
print (nums1)

#Write a Python program that removes all duplicates from a given list and prints the new list without duplicates.
stationary:list = ["pen", "paper", "ink", "paper","notepad"]
new_list = list(set(stationary))
print (new_list)

#Create a dictionary where the keys are the names of 5 different countries and the values are their capitals. Write a program to display all the countries and their capitals.
capitals_of_countries = {
    "Pakistan": "Islamabad",
    "Japan": "Tokyo",
    "Germany": "Berlin",
    "India": "Delhi",
    "Iran": "Tehran",
} 
for country, capital in capitals_of_countries.items():
    print (f"The capital of {country} is {capital}")      
    
#Write a program to update the 'grade' value to 'A', and add a new key-value pair for 'major' with the value 'Computer Science'.
student = {'name': 'John', 'age': 22, 'grade': 'B'}
student['grade'] = 'A'
print (student)
student['major'] = 'computer science'
print (student)

#Write a program that creates a dictionary where the keys are subjects (e.g., 'Math', 'Science') and the values are lists of marks. Add marks for 3 subjects, and print the average marks for each subject.
Marks = {'math': 77, 'science': 89,}
Marks.update ({'physics': 98, 'chemistry': 65, 'biology': 95})
print (Marks)
total_marks = sum (Marks.values())
total_subjects = len (Marks)
Average_result = total_marks/ total_subjects
print(Average_result)

