#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Assignment 2 of Data Science Masters 2.0
# Q1. How do you comment code in Python? What are the different types of comments?
"""
Two ways to do it 
first single line comment # this is comment 
second multi line comment """this is also a comment"""
"""


# In[1]:


#Q2. What are variables in Python? How do you declare and assign values to variables?
"""Variables is a container which stores data this could be type integer, floating, string, char, bool etc.
"""
# assigning the  variables we can simply use assigning operator (=)
a = 3 #integer type
b = 3.14 # floating type
c = "string"
d = True
e = 'A'


# In[3]:


#Q3. How do you convert one data type to another in Python?
# we use type casting to do it 
a = 2
b = 4
str(a)+str(b)


# In[4]:


#Q4. How do you write and execute a Python script from the command line?
"""To write a Python script, you can use any text editor to create a new file with the .py extension. Then, you can write your Python code in the file and save it.
To execute the script from the command line, you need to open a terminal or command prompt and navigate to the directory where your script is saved. Then, you can run the script by typing python followed by the name of your script file and pressing enter. For example, if your script is named myscript.py, you would type python myscript.py and press enter."""


# In[7]:


#Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].
my_list = [1, 2, 3, 4, 5]
sub_list = my_list[1:3]
print(sub_list)


# In[8]:


#Q6. What is a complex number in mathematics, and how is it represented in Python?
# in mathematics complex number is represented like 3 + 4j
x = 3 + 4j
print(x.real) # Output: 3.0
print(x.imag) # Output: 4.0


# In[9]:


#Q7. What is the correct way to declare a variable named age and assign the value 25 to it?
age = int(25)


# In[10]:


#Q8. Declare a variable named price and assign the value 9.99 to it. What data type does this variable belong to?
price = 9.99
type(price)


# In[11]:


#Q9. Create a variable named name and assign your full name to it as a string. How would you print the value of this variable?
name = "Ankit Sharma"
name 
print(name)


# In[13]:


#Q10. Given the string "Hello, World!", extract the substring "World".
string = "Hello, World!"
# first way
substring = string[7:12]
print(substring)
# second way
substring = string.split(',')
substring[1]


# In[14]:


#Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are currently a student or not.
is_student = True
is_student = False

