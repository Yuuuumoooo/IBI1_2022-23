# What does this piece of code do?
# Answer: Get 10 random values between 1 and 100, and take the largest 
# value among these 10 random numbers.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint
#import the function "randint" from the library "random"


# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
stored_random_number=0
while progress<10:
	progress+=1
#loop 10 times
	n = randint(1,100)
	if n > stored_random_number:
		stored_random_number = n
#take the larger value 
print(stored_random_number)