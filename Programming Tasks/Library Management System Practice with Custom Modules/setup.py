# setup.py

from setuptools import setup , find_packages

setup(
    name = 'mylibrary',
    version = '0.1',
    packages = find_packages(),
    description = 'A simple library management system',
    author =  'Shayan'
    author_email = 'fcshayan20@gmail.com'
    classifiers = [
    'programming language ::python::3',
    'operating system :: Os Independent',
    ],
    python_requires = '>=3.6',
)