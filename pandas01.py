# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:12:48 2024

@author: saari
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

print(file.info())

#object - string -text in pandas

print(file.describe())

file = pandas.read_csv("iris.csv")

print(file)
print(file.info())
print(file.describe())

file = pandas.read_csv("diab_data.csv")
print(file)
print(file.info())
print(file.describe())

file = pandas.read_csv("housing_data.csv")
print(file)
print(file.info())
print(file.describe())
#no column names

#to add the column names
#column_names = ["A","B","C"....]
#file = pandas.read_csv("housing_data.csv", names = column_names )

print("insurance file")
#file = pandas.read_csv("insurance_data.csv",header=[4])

file = pandas.read_csv("insurance_data.csv", skiprows=5)

print(file)
print(file.info())
print(file.describe())

"""
to read a txt file
with semicolon delimiter

file = pandas.read_csv("Geospatial Data.txt", sep =";")
print(file)

file in another directory
file = pandas.read_csv("chat_files/Network_data.csv")

"""








































