import custom_package

# Run function from custom_package directly
print("Run a function from a custom package:")
custom_package.print_text('Hello World!')

# Make a class from custom_package directly
print("Create an instance of a class variable from MyClass located in a custom package.")
instance = custom_package.MyClass(value='Hello World Attribute!')
print(instance.attribute)

# Create a child class of MyClass
instance = custom_package.ChildClass(value='Hello World Attribute!')
print(instance.attribute)

# Note:
# Without using __init__ in custom_package
import custom_package.utils
from custom_package.my_class import MyClass

custom_package.utils.print_text('Hello World!')

instance = MyClass(value='Hello World Attribute!')
print(instance.attribute)