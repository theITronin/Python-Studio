# 1. Module Exploration with dir() 
# The dir() function returns an alphabetized list of all entities (functions, 
# classes, variables) contained inside an imported module.
import os
print(dir(os))  # Prints everything available inside the 'os' module


# 2. Modules vs Packages 
# Module: A single file containing related functions, variables, or constants.
# Package: A container/folder grouping multiple related modules under one name.
# It can be distributed as a directory tree structure or packed inside a .zip file.
# In this example, 'xml' is the package and 'etree' is the module.
from xml import etree
import xml.etree

# 3. Bytecode Compilation (__pycache__) 
# During the very first import of a module, Python translates its source code (.py) 
# into a semi-compiled bytecode format stored in .pyc files.
# These files are placed inside a folder named '__pycache__' at the module's root 
# directory to speed up subsequent loads.


# 4. Private Entities (Naming Conventions)
# To indicate that a specific entity should be treated as private (internal use only), 
# prefix its name with a single underscore '_' or double underscore '__'.
# Note: This is a convention/recommendation for other developers, not a strict access restriction.
_private_variable = "Internal use"
__very_private_variable = "Stronger internal convention"


# 5. The Shebang (#!)
# Terms like shabang, shebang, hasbang, poundbang, or hashpling describe the '#!' digraph.
# It is placed on the very first line of a script to tell Unix-like systems (Linux/macOS) 
# which interpreter to use to execute the file. It has no effect on MS Windows.
#!/usr/bin/env python3


# 6. Custom Package Paths (sys.path)
# If you need Python to recognize and import a package from a non-standard directory, 
# you must append or insert its folder path into the 'sys.path' directory list.
import sys
# sys.path.append("/path/to/custom/location")


# 7. Package Initialization (__init__.py)
# The '__init__.py' file runs implicitly when its containing package is imported.
# It is used to initialize the package and its subpackages. 
# This file can be completely empty, but it must be present in the directory.


# 8. PyPI (The Python Package Index) 
# PyPI (also nicknamed "The Cheese Shop") is the official public repository 
# designed to collect, store, and share free third-party Python packages.
# URL: https://pypi.org/


# 9. Package Management with pip
# 'pip' is a specialized command-line tool used to download and install packages from PyPI.
# It may not always come pre-installed with standard Python distributions on some systems.


# 10. Checking pip Version
# To verify which pip version is active on your operating system, execute either 
# of these commands directly in your system terminal (not inside Python):
# pip --version
# pip3 --version


# 11. Core pip Commands
# Executed in the system console/terminal:
# pip help command      -> Shows a brief description and help for a specific command.
# pip list              -> Displays a list of all currently installed packages.
# pip show package_name -> Displays details and dependencies of a specific package.
# pip search string     -> Searches PyPI directories for packages containing the text string.
# pip install name      -> Installs a package system-wide (requires admin privileges).
# pip install --user name -> Installs a package only for the current local user.
# pip install -U name   -> Upgrades a previously installed package to its latest version.
# pip uninstall name    -> Uninstalls a previously installed package from the environment.