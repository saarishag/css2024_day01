# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:40:42 2024

@author: saari
"""

"""
Storing data in Python
1. Lists
2. Dictionaries 
3. Data Frames -specific to pandas
"""

import pandas 

#import pandas as pd

file = pandas.read_csv("country_data.csv")
print(file)

age1 = 30
age2 = 25
age3 = 29

age = [30,25,29,46,22]

print(age)

print(age[0])
"""
access indiv values of a list
30
"""
print(age[1])
"""
25
"""

"""
all built into python 
"""
print(min(age))
print(max(age))
print(sum(age))

print(len(age))
 
avg = sum(age)/len(age)
print(avg)

g1 = "M"
g2 = "F"
g3 = "M"

gender = ["M", "F", "M"]

c1 = "South Africa"
c2 = "Lesotho"

country_list = ["South Africa","Lesotho"]

"""
print a range of numbers
second number excluded 
"""
print(age[0:3]) 

"""
insert and append values
"""

age.append(100)

print(age)


age.insert(0,100)

print(age)

"""
Dictionaries - key:value pairs 

cat : "a cute animal"

"""

mammals = {"cat" : "a cute animal", "lion": "king of the jungle",
           "elephant":"a gigantic herbivore"}

print(mammals["cat"])

"""
Data frames
"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
'fruits' : fruits,
'sizes' : size_nm
}

#print(fruit_sizes['fruits'])

"""
df = dataframe
"""


import pandas as pd
df = pd.DataFrame(fruit_sizes)

pd.DataFrame.iteritems = pd.DataFrame.items


print(df['fruits'])

print(df['sizes'])

print(df['sizes'].min())

print(df['sizes'].mean())


print(df.describe())

print(df[df['sizes'] > 10]) #subset of data

print(df[1:3]) #range of rows

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices

df.drop(columns=["sizes"], inplace = True)






















