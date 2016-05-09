# Practice 3
# 1. Generate 1~n numbers in list but place them in random order, and remove one of the number
# 2. Use a function to find out which is the removed number
# is this o(n) space with o(n) speed?

import random

# Create a function for item 1
def random_list(n):
    r_list = range(1, n + 1)
    random.shuffle(r_list)
    r_list.remove(random.choice(r_list))
    return r_list

# Find out which number is popped out
def find_item(f_list):
    for y in range(1, len(f_list) + 2):
        if y not in f_list:
            return y

# Ask user to enter a number for list range
n = int(raw_input("Enter the maximum number of the random list you like to generate: "))
final_list = random_list(n)
print "Your random list with one item hidden:", final_list
print "The hidden number is:", find_item(final_list)
