import csv
import string
import math

# Open the CSV File and read it in.
f = open('countries.csv')

randomNums = f.read()
countries = randomNums.split('\n')
length = len(countries)

# Start your search algorithm here.
searchKey = input("What country are you looking for?: ")


notFound = True
first = 0
last = len(countries)-1


while (first <= last and notFound):
    midPoint = int((first + last) / 2)
    if (searchKey == countries[midPoint]):
        notFound == False
    elif(searchKey < countries[midPoint]):
        last = midPoint -1
    elif(searchKey > countries[midPoint]):
        first = midPoint +1

if (notFound == False):
    print("Your country is here!")
else:
    print("Your country isn't here!")
