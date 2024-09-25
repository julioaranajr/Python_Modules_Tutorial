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


def self_test():
    """Run self_test() to test the functions in module1.py."""
    print("Running self_test() in module1.py")
    func1()
    func2()
    print("self_test() in module1.py completed.")


def func1():
    """Function 1 of module 1."""
    print("func1() in module1.py")


def func2():
    """Function 2 of module 1."""
    print("func2() in module1.py")


def greet():
    """Returns a greeting message from Module 1."""
    return "Hello from Module 1"
