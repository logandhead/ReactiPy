from setuptools import setup



setup(
    name='ReactiPy',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1',

    description='Compiles React Components server side using python',

    # The project's main homepage.
    url='https://github.com/logandhead/sampleproject',

    # Author details
    author='Logan Head',
    author_email='logandhead@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
    ],

    # What does your project relate to?
    keywords='react jsx compile react.js reactjs facebook',


    package_data={
        'reactipy': [
            'reactipy/package.json',
            'reactipy/reactipy.js',
        ]
    },

    install_requires=['nodeenv==0.13.1'],


)