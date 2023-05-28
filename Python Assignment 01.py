#!/usr/bin/env python
# coding: utf-8

# # WELCOME TO ASSIGNMENT 01 MASTER OF DATA SCIENCE COURSE 2.0

# In[19]:


"""
Q1. Create one variable containing following type of data:
(i) string
(ii) list
(iii) float
(iv) tuple
"""
a='Masters of data science'
b=[1,2,3,4.5,'5355', 4+5J]
c=5.4
d=("4.4", "Ankit")
print(type(a), type(b),type(c),type(d))


# In[25]:


"""
Q2. Given are some following variables containing data:
(i) var1 = ‘ ‘
(ii) var2 = ‘[ DS , ML , Python]’
(iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
(iv) var4 = 1.
What will be the data type of the above given variable.
"""
var1 = ''
var2 = '[ DS , ML , Python]'
var3 = [ 'DS','ML','Python']
var4 = 1.
print(type(var1), type(var2), type(var3), type(var4))


# In[26]:


"""
Q3. Explain the use of the following operators using an example:
(i) /
(ii) %
(iii) //
(iv) **
"""
example1 = 2/3
example2 = 2%1
example3 = 2//3
example4 = 2**3
print(type(example1), type(example2), type(example3), type(example4))


# In[28]:


"""
Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
element and its data type.
"""
list1 = ["Ankit", 1, ["Number", 1 ,"mein"], 24.32, "kagd",245, 354,"wrw",35,"12"]
for i in list1:
    print(i, type(i))


# In[29]:


"""Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
times it can be divisible."""
a = int(input("enter a number = "))
b = int(input("enter from which you want to divide the above = "))
count = 0
while(a%b==0):
    a/=b
    count+=1
print("Number A is divisible by number B", count, "times.")


# In[30]:


"""Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
divisible by 3 or not."""
numbers = [7, 12, 21, 34, 42, 51, 63, 78, 84, 95, 102, 117, 125, 138, 147, 156, 168, 177, 185, 198, 204, 216, 225, 237, 244]
for i in numbers:
    if i % 3 == 0:
        print(i, "is divisible by 3")
    else:
        print(i, "is not divisible by 3")


# In[32]:


"""Q7. What do you understand about mutable and immutable data types? Give examples for both showing
this property."""
# mutable
# list
list1 = [24, 353, 353, 57]
list1[0] = 34
print(list1)
# string immutable
string = str(list1)


# In[33]:


string[0] ="3q53"


# In[ ]:




