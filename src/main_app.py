"""Main application module to demonstrate package1 and package2.

This module imports functions from package1 and package2 to
print greeting and farewell messages.

It also demonstrates the use of the __import__ function to
dynamically import modules and the use of special attributes
like __file__ and the dir() function to inspect module attributes.

Functions:
    main(): Entry point of the application.
    Prints greeting and farewell messages.

Usage:
    Run this module as the main program to see the output of
    the greeting and farewell messages, along with the file paths and
    attributes of the imported packages.
"""

from package1.module1 import greet as hello
from package1.module1 import self_test as test

from package2.module2 import farewell as bye

# __import__ is a built-in function that imports a module
package1 = __import__("package1")
package2 = __import__("package2")

author = package1.module1.AUTHOR
url = package1.module1.URL


def main():
    """Entry point of the application."""
    print(hello())
    print(test())
    print(bye())


if __name__ == "__main__":
    main()
    # __file__ is a special attribute that returns the path of the module
    print(f"package1: {package1.__file__}")
    print(f"package2: {package2.__file__}")
    # dir() returns a list of valid attributes for the object
    print(dir(package1))
    print(dir(package2))
