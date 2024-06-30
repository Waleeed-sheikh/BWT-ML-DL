# Tasks 1:
# 1. Define a class `Book` with attributes `title`, `author`, and `pages`. Include methods to get and set these attributes.
# 2. Create an instance of `Book` and demonstrate the use of getter and setter methods.
# 3. Implement a class method in the Book that calculates the reading time based on an assumed reading speed (e.g., 250 words per minute).
# 4. Implement inheritance by creating a subclass `Ebook` that inherits from `Book` and adds an attribute `format`. Override the `__str__()` method to display all attributes.



class Book:
    def __init__(self, title, author, pages):
        """
        Initializes a instance of a book
        initializing is done through dunder method(double underscore)
        it is different from java as it is a part of oop in python

        Parameters:
        title : The title of the book. (string)
        author (str): The author of the book.(string)
        pages (int): The number of pages in the book.(int)
        """
        self._title = title
        self._author = author
        self._pages = pages

    def get_title(self):
        """Returns the title of the book."""
        return self._title

    def set_title(self, title):
        """Sets the title of the book."""
        self._title = title

    def get_author(self):
        """Returns the author of the book."""
        return self._author

    def set_author(self, author):
        """Sets the author of the book."""
        self._author = author

    def get_pages(self):
        """Returns the number of pages in the book."""
        return self._pages

    def set_pages(self, pages):
        """Sets the number of pages in the book."""
        if not isinstance(pages, int) or pages < 0:
            raise ValueError("Pages must be a non-negative integer.")
        self._pages = pages

    @classmethod
    def reading_time(cls, pages, words_per_minute=250):
        """
        Calculates the reading time based on an assumed reading speed.

        Parameters:
        pages (int): The number of pages in the book.

        words_per_minute (int): The assumed reading speed in words per minute.
        parameter is assigned a default value of 250. This is done to provide 
        a reasonable default reading speed if no specific speed is provided 
        when the method is called.
      

        Returns:
        float: Estimated reading time in minutes.
        """
        # Assuming an average of 300 words per page.
        words_per_page = 300
        total_words = pages * words_per_page
        return total_words / words_per_minute

    def __str__(self):
        """Returns a string representation of the book."""
        return f"Book: {self._title}, Author: {self._author}, Pages: {self._pages}"


class Ebook(Book):
    def __init__(self, title, author, pages, format):
        """
        Initializes an Ebook instance.

        Parameters:
        title (str): The title of the ebook.
        author (str): The author of the ebook.
        pages (int): The number of pages in the ebook.
        format (str): The format of the ebook (e.g., PDF, EPUB).
        """
        super().__init__(title, author, pages) #function called from the parent class
        self._format = format

    def get_format(self):
        """Returns the format of the ebook."""
        return self._format

    def set_format(self, format):
        """Sets the format of the ebook."""
        self._format = format

    def __str__(self):
        """Returns a string representation of the ebook."""
        return f"Ebook: {self._title}, Author: {self._author}, Pages: {self._pages}, Format: {self._format}"


# Demonstration of the Book and Ebook classes
"""The line if __name__ == "__main__": is a common construct in Python scripts. 
It allows code to be run conditionally, depending on whether the script is being run as the main program or being imported as a module into another script.
 This was different for me as i saw something like this for the first time.
"""
if __name__ == "__main__":
    
  
    # Create an instance of Book
    my_book = Book("THE SHINING", "STEPHEN KING", 328)
    print(my_book)

    # Use getter methods
    print("Title:", my_book.get_title())
    print("Author:", my_book.get_author())
    print("Pages:", my_book.get_pages())

    # Use setter methods
    my_book.set_title("PHOENIX: RISE FROM ASHES")
    my_book.set_author("WALEED SHEIKH")
    my_book.set_pages(112)
    print(my_book)

    # Calculate reading time
    print("Estimated reading time:", Book.reading_time(my_book.get_pages()), "minutes")

    # Create an instance of Ebook
    my_ebook = Ebook("Sapiens", "Yuval Noah Harari", 443, "EPUB")
    print(my_ebook)

    # Use getter and setter for format
    print("Format:", my_ebook.get_format())
    my_ebook.set_format("PDF")
    print(my_ebook)







