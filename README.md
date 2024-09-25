# Python Module Tutorial

## Table of Contents

1. [Introduction](#introduction)

2. [Python Modules](#python-modules)

3. [Creating a Module](#creating-a-module)

4. [Using a Module](#using-a-module)

5. [Re-naming a Module](#re-naming-a-module)

6. [Built-in Modules](#built-in-modules)

7. [Using the dir() Function](#using-the-dir-function)

8. [Import From Module](#import-from-module)

9. [Creating an Alias](#creating-an-alias)

10. [Convention for Importing Modules](#convention-for-importing-modules)

11. [Summary](#summary)

## Introduction

In this tutorial, we will learn about Python modules. A module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended. Within a module, the module's name (as a string) is available as the value of the global variable `__name__`.

## Python Modules

A module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended. Within a module, the module's name (as a string) is available as the value of the global variable `__name__`.

## Creating a Module

To create a module, you just need to save the code you want in a file with the file extension `.py`. For example, we can create a module named `module1.py` with the following content:

```python
def greeting(name):
  print("Hello, " + name)
```

## Using a Module

Create a new Python file and import the module we just created:

```python
import module1

module1.greeting("Jonathan")
```

When using a function from a module, use the syntax: `module_name.function_name`.

## Re-naming a Module

You can create an alias when you import a module, by using the `as` keyword:

```python
import module1 as mx

mx.greeting("Jonathan")
```

## Built-in Modules

There are several built-in modules in Python, which you can import whenever you like. For example, the `platform` module:

```python
import platform

x = platform.system()
print(x)
```

## Using the dir() Function

There is a built-in function to list all the function names (or variable names) in a module. The `dir()` function:

```python
import platform

x = dir(platform)
print(x)
```

output:

```python
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_ironpython', '_sys_version', '_sys_version_cache', 'architecture', 'dist', 'java_ver', 'libc_ver', 'linux_distribution', 'mac_ver', 'machine', 'node', 'popen', 'platform', 'processor', 'python_build', 'python_compiler', 'python_implementation', 'python_revision', 'python_version', 'python_version_tuple', 're', 'release', 'system', 'system_alias', 'uname', 'uname_result', 'version', 'win32_ver']
```

## Import From Module

You can choose to import only parts from a module, by using the `from` keyword:

```python
from module1 import greeting

greeting("Jonathan")
```

## Creating an Alias

You can create an alias when you import a module, by using the `as` keyword:

```python
from module import greeting as gm

gm("Jonathan")
```

## Convention for Importing Modules

It is a common convention to use lowercase letters for the module name. If you create a module name with a capital letter, it will still work, but it is not recommended.

Relative imports for intra-package imports are highly discouraged. Always use the absolute package path for all imports.

e,g, `from package import module` is recommended over `from . import module`.

## package1/module1.py

```python
def greet():
    return "Hello from Module 1"
```

## package2/module2.py

```python
def farewell():
    return "Sayonara from Module 2"
```

## main_app.py

```python
from package1.module1 import greet
from package2.module2 import farewell

def main():
    print(greet())
    print(farewell())

if __name__ == "__main__":
    main()
```

## Instructions

1. Create the directory structure as shown above.
2. Add the provided code snippets to their respective files.
3. Run `main_app.py` to see the output.

## Summary

In this tutorial, you learned about Python modules. A module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended. Within a module, the module's name (as a string) is available as the value of the global variable `__name__`.

You also learned how to create a module, use a module, re-name a module, use built-in modules, use the `dir()` function, import from a module, create an alias, and the convention for importing modules.

## References

- [Python Modules](https://www.w3schools.com/python/python_modules.asp)
- [Python Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Modules](https://realpython.com/python-modules-packages/)
- [Python Modules](https://www.learnpython.org/en/Modules_and_Packages)
- [Python Modules](https://www.programiz.com/python-programming/modules)
- [Python Modules](https://www.geeksforgeeks.org/modules-in-python/)
