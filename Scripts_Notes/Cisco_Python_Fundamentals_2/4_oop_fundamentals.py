# 1. Classes vs Objects & Basic Definition
# A class is an abstract idea/blueprint used to instantiate multiple objects.
# An object is a concrete incarnation equipped with an identifying name, 
# a set of properties (variables), and a set of methods.
class ThisIsAClass:
    pass  # The 'class' keyword defines a new class

this_is_an_object = ThisIsAClass()  # Instantiating an object using function syntax


# 2. OOP Paradigms: The Stack Example
# A stack is a LIFO (Last In, First Out) data structure requiring push() and pop().
# Implementing a stack procedurally presents data security flaws. OOP solves 
# this by encapsulating data and operations inside a single object entity.


# 3. Methods, Constructors & The 'self' Parameter
# Methods are functions declared inside a class that access class components.
# The '__init__' method acts as the constructor, responsible for creating objects.
# Every method declaration must have 'self' as its first parameter to refer 
# to the specific object instance invoking it. Constructors cannot return values.


# 4. Encapsulation & Private Components (Name Mangling)
# Prefixing a component name with a double underscore '__' makes it private.
# Private elements cannot be accessed directly from the outside, but they can still 
# be reached via a mangled name: _ClassName__PrivatePropertyName.


# 5. Instance vs Class Variables and __dict__
# Instance Variables: Properties attached to a specific object. Stored in the 
# object's individual '__dict__' dictionary. Can be dynamically added/removed.
# Class Variables: A single copy shared among all instances. Exists even if no 
# objects are created. Stored in the class's own separate '__dict__' dictionary.

class Sample:
    gamma = 0  # Class variable (shared, not in object's __dict__)
    
    def __init__(self):
        self.alpha = 1       # Public instance variable
        self.__delta = 3     # Private instance variable (will be mangled)

obj = Sample()
obj.beta = 2  # Dynamic instance variable added during lifetime only to 'obj'

print(obj.__dict__)  # Output: {'alpha': 1, '_Sample__delta': 3, 'beta': 2}


# 6. Property Verification with hasattr()
# hasattr(target, 'property') checks if an object or class contains a specific entity.
print(hasattr(obj, "alpha"))  # Output: True
print(hasattr(Sample, "gamma"))  # Output: True


# 7. Built-in Class Properties
# All classes (not instances) contain introspection attributes:
# __name__: Stores the string name of the class.
# __module__: Stores the name of the module where the class is defined (__main__ if local).
# __bases__: A tuple containing the direct superclasses of the class.

class InfoSample:
    def __init__(self):
        self.name = InfoSample.__name__
        
    def display_info(self):
        print("Name: " + self.name + " | Module: " + InfoSample.__module__)

obj_info = InfoSample()
obj_info.display_info()  # Output: Name: InfoSample | Module: __main__
print(InfoSample.__bases__)  # Output: (<class 'object'>,)