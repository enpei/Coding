# Practice 4
# 1. Generate 1~n numbers in list but place them in random order, and remove one of the number
# 2. Use a function to find out which is the removed number
# Rewrite practice 3 in find_item() that write our own sort method

import random

# Create a function for item 1
def random_list(n):
    r_list = range(1, n + 1)
    random.shuffle(r_list)

    # Randomly remove one of numbers in r_list
    r_list.remove(random.choice(r_list))
    return r_list

# Find out which number is popped out
def find_item(f_list):
    # Bubble Sort
    a = 0
    # Exit while loop if no swap is made throughout the whole list
    while a < len(f_list) - 1:
        a = 0
        for x in xrange(len(f_list) - 1):
            if f_list[x] > f_list[x + 1]:
                tep = f_list[x + 1], f_list[x]
                f_list[x], f_list[x + 1] = tep
            else:
                a += 1

    # Find the removed number from sorted f_list
    # If last number is not equal to what list range user enters(whihc is n), that will be the removed one.
    if f_list[len(f_list) - 1] != len(f_list) + 1:
        return len(f_list) + 1

    # If first number is not 1, 1 will be the removed one.
    elif f_list[0] != 1:
        return 1

    # If f_list[x + 1] - f_list[x] over 1, their average will be the removed one.
    else:
        for x in range(len(f_list) - 1):
            if f_list[x + 1] - f_list[x] > 1:
                return (f_list[x + 1] + f_list[x]) / 2


# Ask user to enter a number for list range
n = int(raw_input("Enter the maximum number of the random list you like to generate: "))
final_list = random_list(n)
print "Your random list with one item hidden:", final_list
print "The hidden number is:", find_item(final_list)