# Question 4
# Write a code that will:
# 1. Contains a function `find_max_min(numbers_list)` that takes a list of numbers and returns both the maximum and minimum numbers in the list.
# 2. Prompts the user to enter 5 numbers, stores them in a list, and then uses the `find_max_min` function to find and display the maximum and minimum numbers.




def findMaxMin(numbers):
    return max(numbers),min(numbers)

# Prompt the user to enter numbers separated by spaces
user_input = input("Enter 5 numbers separated by spaces: ")


#numbers = [int(num) for num in user_input.split()]
# This question took me a while because the above piece of code on how to make a list from for loop within a loop confused me
#then to make it simpler i divided it into 2 parts
#first i simply split the user number into a list
#then i made a list from that spliced list in another line

stringArray=user_input.split()
myList=[int(number) for number in stringArray]

max , min=findMaxMin(myList)
print(max,min)
