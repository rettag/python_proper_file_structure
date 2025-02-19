# This file should be treated as the core/basic functions to use in the package.
# Hence, why it is named 'utils' -- It is short for 'utilities'
# 'utils.py' is a common and standard filename to be inside of packages.

# More functions can be created inside of the custom_package folder.
# Oddly, you can add subpackages inside this package. It will always follow the same structure as this one.
# Make sure to always import them inside of __init__.py to follow proper file organization!


# A function created inside of utils.py
def print_text(text):
    """
    Args:
        text (str): the text wanting to be printed

    Return:
        Nothing.
    """
    print(text)