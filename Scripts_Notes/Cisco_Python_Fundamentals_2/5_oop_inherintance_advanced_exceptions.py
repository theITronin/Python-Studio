# 1. Inheritance Concepts & Diagrams
# When a class derives from another, the relation is called Inheritance.
# Superclass (Parent): Present on top. / Subclass (Child): Derived class below.
# In inheritance diagrams, arrows direct from the Subclass towards its Superclass.
# Subclasses automatically inherit all methods, class variables, and instance variables.


# 2. String Representation: __str__()
# Redefining the __str__() method customizes how an object converts into a readable string.
class Mouse:
    Population = 0  # Inheritable class variable
    
    def __init__(self, name):
        Mouse.Population += 1
        self.name = name
        
    def __str__(self):
        return "Hi, my name is " + self.name

class LabMouse(Mouse):
    pass  # Automatically inherits everything from Mouse

professor_mouse = LabMouse("Professor Mouse")
print(professor_mouse)  # Invokes __str__ automatically. Output: Hi, my name is Professor Mouse
print(Mouse.Population)  # Output: 1


# 3. Introspection & Object Relations
# issubclass(C1, C2): Returns True if Class_1 is a subclass of Class_2.
# isinstance(O, C): Returns True if Object belongs to Class or its subclasses.
# 'is' operator: Checks if two variables refer to the exact same object in memory.

class ExtMouse(Mouse): pass

mickey = Mouse("Mickey")
cloned_mickey = mickey
minnie = Mouse("Minnie")

print(issubclass(LabMouse, Mouse))   # Output: True
print(isinstance(mickey, LabMouse))   # Output: False
print(mickey is minnie)              # Output: False
print(mickey is cloned_mickey)       # Output: True


# 4. The super() Function & Overriding
# super() returns a reference to the nearest superclass.
# Subclasses can override parent methods by declaring an identical name.

class AncientMouse(Mouse):
    def __str__(self):
        # Overrides the parent __str__ method completely
        return "Meum nomen est " + self.name

class EnhancedLabMouse(Mouse):
    def __str__(self):
        # Uses super() to extend parent functionality instead of erasing it
        return "Laboratory " + super().__str__()

print(AncientMouse("Caesar"))        # Output: Meum nomen est Caesar
print(EnhancedLabMouse("Brain"))     # Output: Laboratory Hi, my name is Brain


# 5. Property Resolution Order (MRO)
# To locate any property, Python scans components in this exact order:
# 1. Inside the object itself.
# 2. Inside all classes in the inheritance chain from bottom to top.
# 3. If multiple parents exist (multiple inheritance), it scans from left to right.
# Failure to find the property raises an AttributeError exception.


# 6. Advanced Exceptions: try-except-else-finally
# else: Executes ONLY if NO exception was raised in the try block.
# finally: ALWAYS executes regardless of whether an exception occurred or not.

try:
    assert __name__ == "__main__"
except AssertionError:
    print("failed", end=' ')
else:
    print("success", end=' ')
finally:
    print("finished")
# Output: success finished


# 7. Exception Objects & Custom Exceptions
# Using 'except ExceptionName as exception_object:' intercepts the error object.
# The object's 'args' property (a tuple) contains arguments passed to its constructor.
# Built-in exception classes can be extended via inheritance to create custom errors.

try:
    raise ValueError("Custom error message", 404)
except ValueError as e:
    print(e.args)  # Output: ('Custom error message', 404)