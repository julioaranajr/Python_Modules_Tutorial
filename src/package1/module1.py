"""
This module, located at /Python_Modules_Tutorial/src/package1/module1.py.

It provides a set of functions for demonstration purposes.

Functions:
    self_test(): Tests the functions in this module.
    func1(): Prints a message indicating it is function 1.
    func2(): Prints a message indicating it is function 2.
    greet(): Returns a greeting message from Module 1.

Attributes:
    AUTHOR (str): The author of the module.
    URL (str): The URL associated with the author.
"""

AUTHOR = "julioaranajr"
URL = "https://julioaranajr.com/"
USERNAME = input("Enter your username for module1: ")


def self_test(name="Module 1"):
    """Run tests for the functions in module1.py."""
    print(f"Running self_test() in {name}")
    func1()
    func2()
    print(greet())
    print(author(AUTHOR, URL))
    print("self_test() in module1.py completed.")


def func1():
    """Print Function 1 of module 1."""
    print("func1() in module1.py")


def func2():
    """Print Function 2 of module 1."""
    print("func2() in module1.py")


def greet(name=USERNAME):
    """Return a greeting message from Module 1."""
    if name:
        return f"Hello, {name}! Welcome to Module 1."
    else:
        return "Hello! Welcome to Module 1. Anonymous user."


def author(name=AUTHOR, url=URL):
    """Return the author and URL of the module."""
    if name and url:
        print(f"Author: {name}")
        print(f"URL: {url}")
    else:
        print("Author and URL not available.")


def main():
    """Run self_test() in module1.py."""
    self_test()


if __name__ == "__main__":
    main()
