"""Module 2 attributes script.

This script imports `module2` from `package2` and checks for
the presence of a list of attributes in the global namespace
or within `module2`. It prints the value of each attribute if
found, or a "Not found" message if the attribute is not present.

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
- "module2"

Usage:
Run the script to see the values of the specified attributes
in the global namespace or within `module2`.
"""

from package2 import module2

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
    "module2",
]

for attr in attributes:
    if attr in globals():
        print(f"{attr}: {globals()[attr]}")
    elif hasattr(module2, attr):
        print(f"{attr}: {getattr(module2, attr)}")
    else:
        print(f"{attr}: Not found")
