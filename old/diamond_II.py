# Diamond v1.2
# Not sure if this is 0(1) structure acutally....
# No more list now

a = 0
while a == 0:
    try:
        # Ask user to enter a number
        n = int(raw_input('Enter a magic number other than -1 for the diamond: '))
    
        # Endless checking for the number
        if n < 0:
            # If user enter negative number other than -1
            if n != -1:
                print "Hey dude, you know I can't make the diamond for you with this \"Negative\" number! Try again."
            
            #If user enter -1 to exit the program
            else:
                print "We all have a great time, bye bye!"
                a += 1

        # If user enter zero
        elif n == 0:
            print "Seriously?! Try again."

        # Create Diamond and write it into file with "with" statement
        else:
            with open("Diamondv1.2.txt", "a+") as result:
                result.write('Here\'s your lovely %d levels diamond:' % (n * 2 -1) + '\n')
                for x in range(1, n * 2):
                    if x <= n:
                        result.write(' ' * (n-x) + '*' * (x * 2 - 1) + '\n')
                    else:
                        result.write(' ' * abs(n-x) + '*' * ((n * 2 - x) * 2 - 1) + '\n')
                result.write('\n')
            print "See your shining diamond in Diamondv1.2.txt"

    # If user enter string
    except ValueError:
        print "Come on, enter a \"NUMBER\" please:"













