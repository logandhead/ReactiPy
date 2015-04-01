from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='ReactiPy',

    version='0.1.0',

    description='Compiles React Components server side using python',

    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/logandhead/ReactiPy',

    # Author details
    author='Logan Head',
    author_email='logandhead@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
    ],

    # What does your project relate to?
    keywords='react jsx compile react.js reactjs facebook',
    packages=find_packages(),
    package_data={'': ['*.json', '*.js']},
    install_requires=['nodeenv==0.13.1']
)