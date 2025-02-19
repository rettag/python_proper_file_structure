# This is required for portability!
# You can't share this code with anyone if you don't give them instructions on how to set it up and use it!
# This file tells python how your code should be installed

from setuptools import setup, find_packages

setup(
    name="custom_package",
    version="0.1",
    author="Rett Graham",
    author_email="rettg@umich.edu",
    description="An example of a custom package hightlighting proper python file structure and organization.",
    packages=find_packages(),  # Automatically finds "custom_package". This is will you list all packages and subpackages as a list of strings.
    install_requires=[ #"matplotlib", "numpy==1.15.4", COMMENTED OUT FOR QUICKER DOWNLOAD.
        "pycodestyle>=2.4.0"
    ],  # List dependencies here (e.g., ["numpy", "pandas"])
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)


# Now you run in your terminal:
# pip install -e .
# This allows you to have custom_package be imported into your local environment.

# Therefore, if its on your local computer, navigate to that package and pip install -e .
# However, if on github, do pip install [github_repo_link]