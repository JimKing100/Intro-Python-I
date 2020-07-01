# Write a function is_even that will return true if the passed-in number is even.


def even_num(n):
    if (n % 2) == 0:
        result = True
    else:
        result = False
    return result


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if even_num(num) is True:
    print('Even!')
else:
    print('Odd')
