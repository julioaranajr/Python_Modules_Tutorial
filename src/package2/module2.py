"""
Module 2 of package 2.

This module contains the following functions:
- func1: Prints a message indicating it is func1 from module2.py.
- func2: Prints a message indicating it is func2 from module2.py.
- farewell: Returns a farewell message "Sayonara from Module 2".
"""

USERNAME = input("Please, Enter your username for module2: ")


def self_test():
    """Run tests for the functions in module2.py."""
    print("Running self_test() in module2.py")
    func1()
    func2()
    print(farewell())
    print("self_test() in module2.py completed.")


def func1():
    """Print Function 1 of module 2."""
    print("func1() in module2.py")


def func2():
    """Print Function 2 of module 2."""
    print("func2() in module2.py")


def farewell(name=USERNAME):
    """Return a farewell message from Module 2."""
    if name:
        return f"Goodbye, {name}! Sayonara from Module 2."
    else:
        return "Goodbye! Sayonara from Module 2. Anonymous user."


def main():
    """Run self_test() in module2.py."""
    self_test()


if __name__ == "__main__":
    main()
