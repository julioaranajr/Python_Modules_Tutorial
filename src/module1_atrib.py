"""Module1 attributes script.

This script imports `module1` from `package1` and then checks for
the presence of a list of attributes in the global namespace or
within `module1`. It prints the value of each attribute if found,
or indicates that the attribute is not found.

Attributes checked:
- "__builtins__"
- "__cached__"
- "__doc__"
- "__file__"
- "__loader__"
- "__name__"
- "__package__"
- "__path__"
- "__spec__"
- "module1"

Usage:
Run the script to see the values of the specified attributes
in the global namespace or within `module1`.
"""

from package1 import module1

attributes = [
    "__builtins__",
    "__cached__",
    "__doc__",
    "__file__",
    "__loader__",
    "__name__",
    "__package__",
    "__path__",
    "__spec__",
    "module1",
]

for attr in attributes:
    if attr in globals():
        print(f"{attr}: {globals()[attr]}")
    elif hasattr(module1, attr):
        print(f"{attr}: {getattr(module1, attr)}")
    else:
        print(f"{attr}: Not found")
