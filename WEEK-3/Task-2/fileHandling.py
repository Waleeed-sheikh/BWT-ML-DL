# Task 2
# 1. Write a Python program to read data from a text file (`data.txt`) and print its contents.
# 2. Implement exception handling to manage scenarios such as file not found and errors while reading from the file.
# 3. Create a function that writes user input to a new file (`output.txt`) and handles exceptions related to file writing.
# 4. Modify the file reading function to count the number of words in the file and print the result.
# Submission Requirements:
# - Python code file (`file handling.py`) containing the complete program.
# - The code must be well commented.
# - The code must be error-free with the implementation of exceptional handling.


def read_file(file_name):
    """
    Reads the content of a file and prints it.
    Also counts and prints the number of words in the file.

    Parameters:
    file_name (str): The name of the file to be read.

    Returns:
    None
    """
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File Contents:")
            #this just prints whatever was in the file.
            print(content)
            
            #  this prints after counting the number of words
            words = content.split()
            word_count = len(words)
            print(f"\nNumber of words in the file: {word_count}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except IOError:
        print(f"Error: An IOError occurred while reading the file '{file_name}'.")


def write_to_file(file_name, content):
    """
    Writes the given content to a file.

    Parameters:
    file_name (str): The name of the file to write to.
    content (str): The content to be written to the file.

    Returns:
    None
    """
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print(f"Content written to '{file_name}' successfully.")
    except IOError:
        print(f"Error: An IOError occurred while writing to the file '{file_name}'.")


# Main program execution
if __name__ == "__main__":
    input_file = 'data.txt'
    
    # Reading from the input file
    read_file(input_file)
    
    # Getting user input to write to the output file
    user_content = input("Enter the content you want to write to output.txt: ")
    
    output_file = 'output.txt'
    write_to_file(output_file, user_content)
  
#this was realtively easy only thing was to just look up for the syntax for exception handling and file read write.
