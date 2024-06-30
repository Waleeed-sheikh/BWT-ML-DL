# . Create an iterator class `Countdown` that counts down from a given number to 1.
# 2. Implement a generator function `fibonacci_generator` that yields Fibonacci numbers up to a specified limit.
# 3. Implement a generator function random_number_generator that yields a sequence of random numbers between a specified range.
# 4. Write a Python program that uses the `Countdown` iterator, `fibonacci_generator` and random_number_generator  to demonstrate their usage


import random
#module to generate random numbers

class Countdown:
    """
    Iterator class that counts down from a given number to 1.
    """
    def __init__(self, start):
        if start < 1:
            raise ValueError("Countdown start must be a positive integer.")
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        current = self.current
        self.current -= 1
        return current

def fibonacci_generator(limit):
    """
    Generator function that yields Fibonacci numbers up to a specified limit.

    Parameters:
    limit (int): The upper limit for the Fibonacci sequence.

    Yields:
    int: The next Fibonacci number.
    """
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

def random_number_generator(start, end, count):
    """
    Generator function that yields a sequence of random numbers within a specified range.

    Parameters:
    start (int): The lower bound of the range.
    end (int): The upper bound of the range.
    count (int): The number of random numbers to generate.

    Yields:
    int: A random number within the specified range.
    """
    if start > end:
        raise ValueError("Start value must be less than or equal to end value.")
    for _ in range(count):
        yield random.randint(start, end)

def main():
    # Demonstrating the Countdown iterator
    print("Countdown:")
    try:
        for number in Countdown(5):
            print(number)
    except ValueError as e:
        print(e)
    
    # Demonstrating the Fibonacci generator
    print("\nFibonacci sequence up to 15:")
    for number in fibonacci_generator(15):
        print(number)

    # Demonstrating the random number generator
    print("\nRandom numbers between 1 and 10 (5 numbers):")
    try:
        for number in random_number_generator(1, 10, 5):
            print(number)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
