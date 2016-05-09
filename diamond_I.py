"""
My first python practice: Diamond Show
Supervised by Walter Chen

"""
# ask user to input dimand levels
n = int(raw_input('How many levels should the diamond be: '))
my_diamond = open("Diamond.txt", "a")


# if user does not enter -1, save dimand in alist
while n != -1 :
    if n > 0 :
        level = n * 2 - 1
        o = n
        alist = range(level)
        print 'You will see the %d levels diamond in Diamond.txt file--- ' % level + '\n'
        for i in range(1, level+1):
            if i <= ((level+1)/2):
                alist[i-1] = ' ' * (n - 1) + '*' * (i * 2 - 1)
                n -= 1
            else:
                alist[i-1] = ' ' * (i - (level+1)/2) + '*' * ((o - 1) * 2 - 1)
                o -= 1

        # output to file
        my_diamond.write("%d levels diamond: " % (level) + '\n')
        for x in alist:
            my_diamond.write(x + '\n')

        # ask user to enter number again
        n = int(raw_input('Want more? Try other levels: '))
    else:
        n = int(raw_input('This is not a valid number, try other levels: '))

else:
    print 'Looks like you are done with it, bye bye!'
    my_diamond.close()









