#!/usr/bin/env python
# coding: utf-8

# In[3]:


num=input("enter the number")
number=num.split()
number=[int(num) for num in number]
for (i=0;i<number;i++)
for(j=1;j<number;j++)
if(int a[i]>a[i+1]):
    int a[i]=a[i
print(num)



# In[ ]:


Certainly! Taking input values in Python for sorting can be done in a few simple steps. Here’s a concise example to guide you:

Example 1: Sorting a List of Numbers
# Taking input from the user
input_values = input("Enter numbers separated by spaces: ")

# Splitting the input string into a list of strings
numbers = input_values.split()

# Converting the list of strings to a list of integers
numbers = [int(num) for num in numbers]

# Sorting the list of numbers
sorted_numbers = sorted(numbers)

# Displaying the sorted list
print("Sorted numbers:", sorted_numbers)

Example 2: Sorting a List of Strings
# Taking input from the user
input_values = input("Enter words separated by spaces: ")

# Splitting the input string into a list of strings
words = input_values.split()

# Sorting the list of words
sorted_words = sorted(words)

# Displaying the sorted list
print("Sorted words:", sorted_words)

Example 3: Sorting a List of Tuples
# Taking input from the user
input_values = input("Enter tuples (e.g., (1,2) (3,4)): ")

# Splitting the input string into a list of tuple strings
tuple_strings = input_values.split()

# Converting the list of tuple strings to a list of tuples
tuples = [eval(tup) for tup in tuple_strings]

# Sorting the list of tuples
sorted_tuples = sorted(tuples)

# Displaying the sorted list
print("Sorted tuples:", sorted_tuples)


Feel free to adapt these examples based on your specific needs. Happy coding!

