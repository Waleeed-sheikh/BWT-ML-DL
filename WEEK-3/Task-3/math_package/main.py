# main.py

from math import addition, subtraction, multiplication, division, modulus, exponentiation, sqrt

def main():
    a = 10
    b = 5
    
    # Demonstrating addition
    print(f"Addition of {a} and {b}: {addition.add(a, b)}")
    
    # Demonstrating subtraction
    print(f"Subtraction of {b} from {a}: {subtraction.subtract(a, b)}")
    
    # Demonstrating multiplication
    print(f"Multiplication of {a} and {b}: {multiplication.multiply(a, b)}")
    
    # Demonstrating division
    try:
        print(f"Division of {a} by {b}: {division.divide(a, b)}")
    except ValueError as e:
        print(e)
    
    # Demonstrating modulus
    print(f"Modulus of {a} and {b}: {modulus.modulus(a, b)}")
    
    # Demonstrating exponentiation
    base = 2
    exponent = 3
    print(f"{base} raised to the power of {exponent}: {exponentiation.power(base, exponent)}")
    
    # Demonstrating square root
    try:
        x = 16
        print(f"Square root of {x}: {sqrt.square_root(x)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
