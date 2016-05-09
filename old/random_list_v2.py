# Practice 3
# 1. Generate 1~n numbers in list but place them in random order, and remove one of the number
# 2. Use a function to find out which is the removed number
# Rewrite practice 2 in find_item() that doesn't user "x in list" method

import random

# Create a function for item 1
def random_list(n):
    r_list = range(1, n + 1)
    random.shuffle(r_list)

    # Randomly remove one of numbers in r_list
    r_list.remove(random.choice(r_list))
    return r_list

# Find out which number is popped out
def find_item(n, f_list):
    # Create a o_list with same length but no number is removed
    o_list = range(1, n + 1)
    
    # Compare each item of o_list in f_list, a n*n solution...  
    for x in range(n):
    	for y in range(n - 1):
			if o_list[x] != f_list[y]:

    			# if sceening all items in f_list and none is the same as o_list[x], it will be the number we are looking for
			    if y == n - 2:
			    	return o_list[x]
			    else:
			    	continue
			else:
				break

# Ask user to enter a number for list range
n = int(raw_input("Enter the maximum number of the random list you like to generate: "))
final_list = random_list(n)
print "Your random list with one item hidden:", final_list
print "The hidden number is:", find_item(n, final_list)
