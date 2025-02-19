# This is how you can setup unit tests. This is done using pytest:
# pip install pytest
# each function must start with an underscore test_
# Note: Always try and test for subcases
# You can separate your tests by putting them in different folders. Here I have test_group_1. 
#I also made a test_group_2. You will see them separated when you run pytest

# Create test functions. Remember to import the code you want to test.
import custom_package # REMEMBER: This won't work unless you pip install -e . your package!

def test_print_text_function():
    test = custom_package.print_text('Hello World Test!')
    compare = print('Hello World Test!')

    assert test == compare


def test_math_function():
    test = 2 ** 2
    answer = 4

    assert test == answer


# Simply type 'pytest' into the terminal to run your tests!
# You can run a folder or file only by giving the directory after: pytest tests/test_group_1/unit_test.py