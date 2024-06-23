# Question 2
# Write a code for a function `Is_even(number)` that will:
# 1. Takes an integer as an input.
# 2. Returns True if the number is even, otherwise False if the number is odd.
# 3. Print whether the number was even or odd

def Is_even(number):
    if number%2==0:
        return True
    else:
        return False

if(Is_even(6)):
    print("the number is even ")
else:
    print(" The number is odd")

#not much to write  straight forward question 
# we can make it more simple by simply sayin return number%2==0 but i thought the above method will be more easily understandable
