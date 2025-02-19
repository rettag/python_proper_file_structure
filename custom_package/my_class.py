# Simular to functions, you can also create classes and them be a part of your packages.
# import this into __init__.py just like you would with functions.

class MyClass:
    """
    A class example
    """

    def __init__(self, value):
        self.attribute = value
        print('parent class!')


class ChildClass(MyClass):
    """""
    A child class of MyClass example
    """""

    def __init__(self, value):
        MyClass.__init__(self, value) # You can do inheritance this way
        super().__init__(value) # This also works. super() is a quick way to inherit the parent class
        print('child class!')
