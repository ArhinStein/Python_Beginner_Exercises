#For for loops create a variable first and then initiate the loop
#Eg:
from numbers import Integral
magicians = ['Alice', 'David', 'Caroline']
for magician in magicians:
    print(magician + " has a wonderful personality" + "\n")
print("Thank you all magicians for your tricks!")

#Making Numerical Lists
for value in range(0,9):
    print(value)

numbers = list(range(0,9))
print(numbers)

#Even Numbers
even_numbers = list(range(2,11,2))
print(even_numbers)

#Increments
#The last digit in the range function...
#is the increment on the range from 2 to 11
increment = list(range(2,11,3))
print(increment)

#Odd Numbers
odd_numbers = [value for value in range(1,20,2)]
print(odd_numbers)

#Empty Function Style 01
squares =[]
for value in range(0,9):
    squares.append(value**2)
print(squares)

#Empty Function Style 02
squares =[]
for value in range(0,9):
    square = value**2
    squares.append(square)
print(squares)

#Empty Function Style 02:List Comprehension
#Concise and precise for most advanved coders.
sqaures = [value**3 for value in range(0,9)]
print(sqaures)

#Simple Statistics with a List of Numbers
##A few Python functions are specific to lists of numbers...
# For example, you can easily find the minimum, maximum,...
#and sum of a list of numbers:
digits = list(range(0,9))
print(min(digits))
print(max(digits))
print(sum(digits))
#Style 01
import numpy 
np_01 = numpy.mean(digits)
np_02 = numpy.median(digits)
print(np_01)
print(np_02)

#Style 02
import numpy as np
print(np.mean(digits))
print(np.median(digits))

